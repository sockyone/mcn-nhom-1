from array import array

class BinaryReader:
    def __init__(self, file_path):
        self.file = open(file_path, "rb")
    

    def close(self):
        self.file.close()
    
    def read_char(self):
        byte = self.file.read(1)
        if byte == b'':
            return False
        else:
            return str(byte, encoding='ascii') 

    def read_int(self):
        # print("im here")
        byte = self.file.read(1)
        if byte == b'':
            return False
        else:
            # print(ord(str(byte, encoding='ascii')))
            return ord(str(byte, encoding='ascii'))

class BinaryWriter:
    def __init__(self, file_path):
        self.file = open(file_path, "wb")
    
    def close(self):
        self.file.close()
    
    def write_char(self, char):
        self.file.write(char.encode(encoding="ascii"))
    
    def write_int(self, integer):
        if integer > 255 or integer < 0:
            raise Exception("Single byte integer can not bigger than 255 and smaller than 0")
        self.file.write(chr(integer).encode(encoding="ascii"))


    