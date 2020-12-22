from binary_operator import *
import sys
# common_dictionary = list(range(256))

# def encode(plain_text: str) -> List[int]:
#     plain_text = plain_text.encode('utf-8')

#     dictionary = common_dictionary.copy()

#     compressed_text = list()
#     rank = 0

#     for c in plain_text:
#         rank = dictionary.index(c)   
#         compressed_text.append(rank)  

#         dictionary.pop(rank)
#         dictionary.insert(0, c)

#     return compressed_text   
# def decode(compressed_data: List[int]) -> str:
#     compressed_text = compressed_data
#     dictionary = common_dictionary.copy()
#     plain_text = []

#     for rank in compressed_text:
#         plain_text.append(dictionary[rank])

#         e = dictionary.pop(rank)
#         dictionary.insert(0, e)

#     return bytes(plain_text).decode('utf-8')

if __name__ == "__main__":
    mode = sys.argv[1]
    input_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    ascii_dictionary = [chr(i) for i in list(range(256))]

    if mode == "e":
        # encode
        binReader = BinaryReader(input_file_path)
        binWriter = BinaryWriter(output_file_path)

        char = binReader.read_char()
        while char:
            rank = ascii_dictionary.index(char)  
            ascii_dictionary.pop(rank)
            ascii_dictionary.insert(0, char)
            binWriter.write_int(rank)

            char = binReader.read_char()
        
        binReader.close()
        binWriter.close()

    elif mode == "d":
        binReader = BinaryReader(input_file_path)
        binWriter = BinaryWriter(output_file_path)

        idx = binReader.read_int()
        # print(idx)
        while True:
            binWriter.write_char(ascii_dictionary[idx])

            e = ascii_dictionary.pop(idx)
            ascii_dictionary.insert(0, e)

            idx = binReader.read_int()
            if type(idx) == bool:
                break

        
        binReader.close()
        binWriter.close()