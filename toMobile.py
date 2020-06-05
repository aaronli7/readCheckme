# All entries in command_package shoud be associated hex number string 
command_package = [
            {
                # Begin to read
                "Command": 'begin_to_read',
                "format": {
                    "CMD_Header": 'AA',
                    "CMD_GET_FILE_START": '03',
                    "~CMD_GET_FILE_START": 'FC',
                    "CMD_PKG_NR": 'ZZZZ',
                    # size of file name:
                    "CMD_BUF_SIZE": '',
                    # file name:
                    "CMD_BUF": '',
                    # CRC checksum
                    "CMD_CRC8": '',
                 }
            },
            {   
                # Read data
                "Command": 'Read data',
                "format": {
                    "CMD_Header": 'AA',
                    "CMD_GET_FILE_DATA": '04',
                    "~CMD_GET_FILE_DATA": 'FB',
                    "CMD_PKG_NR": 'ZZZZ',
                    # size of file name:
                    "CMD_BUF_SIZE": '00',
                    # file name:
                    "CMD_BUF": 'N/A',
                    # CRC checksum
                    "CMD_CRC8": '',
                 }

            },
            {
                # End to read
                "Command": 'End to read',
                "format": {
                    "CMD_Header": 'AA',
                    "CMD_GET_FILE_END": '05',
                    "~CMD_GET_FILE_END": 'FA',
                    "CMD_PKG_NR": 'ZZZZ',
                    # size of file name:
                    "CMD_BUF_SIZE": '00',
                    # file name:
                    "CMD_BUF": 'N/A',
                    # CRC checksum
                    "CMD_CRC8": '',
                 }
            },

            {
                # Ping
                "Command": 'Ping',
                "format": {
                    "CMD_Header": 'AA',
                    "CMD_GET_FILE_END": '15',
                    "~CMD_GET_FILE_END": 'EA',
                    "CMD_PKG_NR": 'ZZZZ',
                    # size of file name:
                    "CMD_BUF_SIZE": '00',
                    # file name:
                    "CMD_BUF": 'N/A',
                    # CRC checksum
                    "CMD_CRC8": '',
                 }
            },

            {
                # get info
                "Command": 'get device info',
                "format": {
                    "CMD_Header": 'AA',
                    "CMD_GET_FILE_END": '14',
                    "~CMD_GET_FILE_END": '14',
                    "CMD_PKG_NR": 'ZZZZ',
                    # size of file name:
                    "CMD_BUF_SIZE": '00',
                    # file name:
                    "CMD_BUF": 'N/A',
                    # CRC checksum
                    "CMD_CRC8": '',
                 }
            },

            {
                # clear all data
                "Command": 'clear all data',
                "format": {
                    "CMD_Header": 'AA',
                    "CMD_GET_FILE_END": '17',
                    "~CMD_GET_FILE_END": '~17',
                    "CMD_PKG_NR": 'ZZZZ',
                    # size of file name:
                    "CMD_BUF_SIZE": '00',
                    # file name:
                    "CMD_BUF": 'N/A',
                    # CRC checksum
                    "CMD_CRC8": '',
                 }
            },

            {
                # Turn off Bluetooth
                "Command": 'turn off bluetooth',
                "format": {
                    "CMD_Header": 'AA',
                    "CMD_GET_FILE_END": '18',
                    "~CMD_GET_FILE_END": '~18',
                    "CMD_PKG_NR": 'ZZZZ',
                    # size of file name:
                    "CMD_BUF_SIZE": '00',
                    # file name:
                    "CMD_BUF": 'N/A',
                    # CRC checksum
                    "CMD_CRC8": '',
                 }
            },

            {
                # reply to begin to read
                "Command": 'reply to begin',
                "format": {
                    "ACK_Header": '55',
                    "ACKCMD_OK or BAD": '00 or 01',
                    "~ACKCMD_OK or BAD": 'FF or FE',
                    "Package number"
                    "ACK_PKT_NR": 'ZZZZ',
                    # size of ACK_BUF:
                    "ACK_BUF_SIZE": '',
                    "ACK_BUF": 'N',
                    # CRC checksum
                    "ACK_CRC8": '',
                 }
            },
            {
                # reply to read
                "Command": 'reply to read',
                "format": {
                    "ACK_Header": '55',
                    "ACKCMD_OK or BAD": '00 or 01',
                    "~ACKCMD_OK or BAD": 'FF or FE',
                    "Package number"
                    "ACK_PKT_NR": 'ZZZZ',
                    # size of ACK_BUF:
                    "ACK_BUF_SIZE": '',
                    # file data
                    "ACK_BUF": 'N',
                    # CRC checksum
                    "ACK_CRC8": '',
                 }
            },
            {
                # reply to end
                "Command": 'reply to end',
                "format": {
                    "ACK_Header": '55',
                    "ACKCMD_OK or BAD": '00 or 01',
                    "~ACKCMD_OK or BAD": 'FF or FE',
                    "Package number"
                    "ACK_PKT_NR": 'ZZZZ',
                    # size of ACK_BUF:
                    "ACK_BUF_SIZE": '',
                    # file data
                    "ACK_BUF": 'N',
                    # CRC checksum
                    "ACK_CRC8": '',
                 }
            },
            {
                # reply to ping 
                "Command": 'reply to Ping',
                "format": {
                    "ACK_Header": '55',
                    "ACKCMD_OK or BAD": '00 or 01',
                    "~ACKCMD_OK or BAD": 'FF or FE',
                    "Package number"
                    "ACK_PKT_NR": 'ZZZZ',
                    # size of ACK_BUF:
                    "ACK_BUF_SIZE": '',
                    # file data
                    "ACK_BUF": 'N',
                    # CRC checksum
                    "ACK_CRC8": '',
                 }
            },

            {
                # reply to info
                "Command": 'reply info',
                "format": {
                    "ACK_Header": '55',
                    "ACKCMD_OK or BAD": '00 or 01',
                    "~ACKCMD_OK or BAD": 'FF or FE',
                    "Package number"
                    "ACK_PKT_NR": 'ZZZZ',
                    # size of ACK_BUF:
                    "ACK_BUF_SIZE": '',
                    # file data
                    "ACK_BUF": 'N',
                    # CRC checksum
                    "ACK_CRC8": '',
                 }
            },
            {
                # reply to clear data
                "Command": 'reply clear data',
                "format": {
                    "ACK_Header": '55',
                    "ACKCMD_OK or BAD": '00 or 01',
                    "~ACKCMD_OK or BAD": 'FF or FE',
                    "Package number"
                    "ACK_PKT_NR": 'ZZZZ',
                    # size of ACK_BUF:
                    "ACK_BUF_SIZE": '',
                    # file data
                    "ACK_BUF": 'N',
                    # CRC checksum
                    "ACK_CRC8": '',
                 }
            },

            {
                # reply to turn off bluetooth
                "Command": 'reply to turn off bluetooth',
                "format": {
                    "ACK_Header": '55',
                    "ACKCMD_OK or BAD": '00 or 01',
                    "~ACKCMD_OK or BAD": 'FF or FE',
                    "Package number"
                    "ACK_PKT_NR": 'ZZZZ',
                    # size of ACK_BUF:
                    "ACK_BUF_SIZE": '',
                    # file data
                    "ACK_BUF": 'N',
                    # CRC checksum
                    "ACK_CRC8": '',
                 }
            },

                
         ]


class MobileModeServer():
    """ Server for checkme pro mobile mode"""


    def __init__(self, name):
        self.name = name
        self.isListen = False
        self.connected_client = None

    def send_response(self, command):
        self._print('got the command from client')

    def start_listen(self):
        self.isListen = True

    def _print(self, msg):
        print('server:', msg)


class MobileModeClient():
    """ Client for checkme pro mobile mode"""
    def __init__(self, name):
        self.name = name
        self.connected_server = None
    
    def scan(self, server):
        if server.isListen == True:
            self._print("connected")
            self.connected_server = server
            self.connected_server._print("connected")
            self.connected_server.connected_client = self
        else:
            self._print("No device found, please make sure server is listening")
    
    def _print(self, msg):
        print('client:', msg)

    def send_command(self, command):
        # combine all the package into a string based on command name: data
        # command = bytes.fromex(data)
        
        self.connected_server.send_response(command)


if __name__ == '__main__':
    
    myClient = MobileModeClient('checkme_client')
    myServer = MobileModeServer('checkme')

myServer.start_listen()
myClient.scan(myServer)

while True:
    command = input("Please type your command")
    myClient.send_command(command)
