"""
This python program is to transfer checkme Pro minimontior data into influxdb.

sample data format (44Byte in total):
Value: 0xA5-5A-2C-01-00-00-00-00-00-00-00-00-00-00-
FF-00-00-00-00-00-00-00-00-00-02-95-00-8A-00-8A-00-
7E-00-7E-00-00-00-00-00-00-00-F1-59-00

bytes: b'A55A2C0100000000000000000000FF0000000000000000000295008A008A007E007E00000000000000F15900'

-------------data structure-----------------------
Key, Byte length, content, index

header, 2, 0xA5 0x5A
Package Size, 1
ECG-Type, 1, 0x01, index: [6:8]
ECG-waveform, 10, short data[5], index: [8:20]
ECG-HR, 2, unsigned short, first byte is valid, index: [20:22] 
ECG-QRS (ms), 2, unsigned short, index: [24:28]
ECG-ST (mv), 2, unsigned short, index: [28:32]
ECG-PVCs, 2, unsigned short
ECG-R wave mark, 1, unsigned short
ECG-note, 1, unsigned short
SpO2-Type, 2, 0x02, index: [48:50]
SpO2-waveform, 10, unsigned short[5], index: [50:72]
SpO2-PR, 2, unsigned short (first byte is valid), index: [72:74]
SpO2-SpO2, 1, unsigned short [76:78]
SpO2-PI, 1, unsigned short [78:80]
SpO2-pulse sound, 1, unsigned short
SpO2-note, 1, unsigned short
other, 1, unsigned short
Battery, 1, unsigned char
CRC checksum, 1, unsigned char
"""
import struct
from bluepy import btle
import binascii
from influxdb import InfluxDBClient
import configparser, json, csv, math, sys, os
import random, time

class MyDelegate(btle.DefaultDelegate):
    def __init__(self, dbClient):
        btle.DefaultDelegate.__init__(self)
        self.dbClient = dbClient

    def handleNotification(self, cHandle, data):
        # convert from binary to hex data
        mydata = binascii.b2a_hex(data)

        print('data notify:', mydata)

        # call save to influxDB function
        self.saveToDB(mydate)

    def _str_to_int(self, s):
        """ Transform hex str into int. """
        i = int(s, 16)
        if i >= 2**7:
            i -= 2**8
        return i
    
    def saveToDB(data):

        #mini monitor data structure
        minimonitor_json_body =[
            {
            "measurement": "random_results",

            "tags":{
                "mode":'miniMonitor',
            },

            # specific data index based on the document of checkme Pro
            "fields":{
                "ECG-HR": int(data[20:22], 16),
                "ECG-QRS": int(data[24:28], 16),
                "ECG-ST": int(data[28:32], 16),
                "SpO2-PR": int(data[72:74], 16),
                "SpO2-SpO2": int(data[76:78], 16),
                "SpO2-SpO2": int(data[78:80], 16),

            },
        
        ]
        self.dbClient.write_points(minimonitor_json_body, time_precision='ms') # millisecond

if __name__ == '__main__':
    heartrate_uuid = btle.UUID('8B00ACE7-EB0B-49B0-BBE9-9AEE0A26E1A3')
    notify_uuid = btle.UUID('0734594A-A8E7-4B1A-A6B1-CD5243059A57')
    
    # Configure the database
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('CEAdb')

# MAC address of your peripheral device
p = btle.Peripheral('E7:CC:E2:D0:5C:C5','random')

# set database client as argument
p.setDelegate(MyDelegate(client))

try:
    print("Setting Characteristics")
    ch = p.getCharacteristics(uuid=heartrate_uuid)[0]
    noti = p.getCharacteristics(uuid=notify_uuid)[0]
    noti_handle = noti.getHandle() + 1

    #enable notification
    setup_data = b"\x01\x00"
    p.writeCharacteristic(noti_handle, setup_data, withResponse=True)

    print("Setting Done, writing now")
    ch.write(struct.pack('<bb', 0x01, 0x00))
    
    print("writing Done, looping now")
    while True:
        if p.waitForNotifications(1.0):
            print("Notification trigger")
            continue
    print("Waiting")

finally:
    p.disconnect()
    print("Disconnected")
