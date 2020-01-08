#code for conversion from hex to base64

#Working:
"""
Character Mapping:
    0 A            17 R            34 i            51 z
    1 B            18 S            35 j            52 0
    2 C            19 T            36 k            53 1
    3 D            20 U            37 l            54 2
    4 E            21 V            38 m            55 3
    5 F            22 W            39 n            56 4
    6 G            23 X            40 o            57 5
    7 H            24 Y            41 p            58 6
    8 I            25 Z            42 q            59 7
    9 J            26 a            43 r            60 8
    10 K            27 b            44 s            61 9
    11 L            28 c            45 t            62 +
    12 M            29 d            46 u            63 /
    13 N            30 e            47 v
    14 O            31 f            48 w
    15 P            32 g            49 x
    16 Q            33 h            50 y
"""

#Algorithm:
"""
The Base64 encoding process is to:

1. Divid the input bytes stream into blocks of 3 bytes.
2. Divid 24 bits of each 3-byte block into 4 groups of 6 bits.
3. Map each group of 6 bits to 1 printable character, based on the 6-bit value using the Base64 character set map.
4. If the last 3-byte block has only 1 byte of input data, pad 2 bytes of zero (\x0000). After encoding it as a normal block, override the last 2 characters with 2 equal signs (==), so the decoding process knows 2 bytes of zero were padded.
5. If the last 3-byte block has only 2 bytes of input data, pad 1 byte of zero (\x00). After encoding it as a normal block, override the last 1 character with 1 equal signs (=), so the decoding process knows 1 byte of zero was padded.
6. Carriage return (\r) and new line (\n) are inserted into the output character stream. They will be ignored by the decoding process.
"""


#generating the character mapping mentioned above.
mapping = {}
mapping.update({key:chr(value) for key,value in zip(range(0,26),range(ord('A'),ord('Z')+1))})
mapping.update({key:chr(value) for key,value in zip(range(26,52),range(ord('a'),ord('z')+1))})
mapping.update({key:value for key,value in zip(range(52,62),range(0,10))})
mapping.update({62:"+",63:"/"})

def hex2bin(hexd):
    binary = ''
    for element in hexd:
        decimal = int(element,16)
        binary += str(format(decimal,"04b"))
    return binary

def bin2map(b):
    dec = int(str(b),2)
    return mapping[dec]

if __name__ == "__main__":

    #hexd = str(input("Enter the Hex String: "))
    hexd = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    length = len(hexd)
    blocks = length//6
    remainder = length%6

    if remainder == 4:
        #pad 1 byte of 0's
        padding = 1
        hexd += "00"
        b64pad = "="
    elif remainder == 2:
        padding = 2
        #pad 2 bytes of 0's
        hexd += "0000"
        b64pad = "=="
    else:
        padding = 0
        b64pad = ""
    
    base64 = ""

    binary = hex2bin(hexd)

    for i in range(0,len(binary),6):
        base64 += str(bin2map(binary[i:i+6]))
    
    base64 += b64pad

    print(base64)

    if base64 == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t":
        print(True)
    else:
        print(False)





        