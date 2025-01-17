import socket
import json
import serial
# server = socket.socket()
# hostname = socket.gethostname()
# port = 12345
# server.bind((hostname, port))
# server.listen(5)

# while True:
#     conn, _ = server.accept()
#     data = conn.recv(1024)
#     print(data.decode())
#     message = 'hello from server'
#     conn.send(message.encode())
#     conn.close()

class server():
    def __init__(self):
        self.server = socket.socket()
        self.hostname = socket.gethostname()
        self.port = 12345
        self.server.bind((self.hostname, self.port))
        self.server.listen(5)
        
    
    def recv(self):
        self.conn, _ = self.server.accept()
        data = self.conn.recv(1024)
        self.conn.close()
        return(data.decode())

    def send(self, target: dict):
        self.conn, _ = self.server.accept()
        data = json.dumps(target).encode()
        data = self.conn.send(data)
        self.conn.close()
        print('call')

        return

class port():
    def __init__(self):
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        except:
            print('No usb device')
        
    
    def recv(self):
        self.ser.reset_input_buffer()
        measure = self.ser.readline().decode('utf-8').rstrip().lstrip('(').rstrip(')')
        return measure

    def send(self, data: dict):
        if data != '':
            target_message = f'<set_pressure {list(data.values())[0]}>'
            print(target_message)
            self.ser.write(target_message.encode())
            print('call')

        return