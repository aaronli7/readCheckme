import struct
from bluepy import btle
import binascii


class MyDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        mydata = binascii.b2a_hex(data)
        # print('Notification: data received: {}'.format(self._str_to_int(mydata)))
        # print("handle:",cHandle)
        print(mydata)

    def _str_to_int(self, s):
        """ Transform hex str into int. """
        i = int(s, 16)
        if i >= 2**7:
            i -= 2**8
        return i


if __name__ == '__main__':
    heartrate_uuid = btle.UUID('8B00ACE7-EB0B-49B0-BBE9-9AEE0A26E1A3')
    notify_uuid = btle.UUID('0734594A-A8E7-4B1A-A6B1-CD5243059A57')

p = btle.Peripheral('E7:CC:E2:D0:5C:C5','random')
p.setDelegate(MyDelegate())

#for i in p.getDescriptors():
for i in p.getCharacteristics():
    print(i)
    if i.supportsRead():
        print(i.read())
    print('handle:', i.getHandle())
    print('\n')
print("Connected")

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
