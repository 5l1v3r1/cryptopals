#same function to convert each bit from binary to hex decimal.
def hex2bin(hexd):
    binary = ''
    for element in hexd:
        decimal = int(element,16)
        binary += str(format(decimal,"04b"))
    return binary


x = hex2bin("1c0111001f010100061a024b53535009181c")
y = hex2bin("686974207468652062756c6c277320657965")

#XOR bitwise
z = ''
for i,j in zip(x,y):
    z += str(int(i)^int(j))

#hexadecimal mapping
mapping = {
    "0000": '0',
    "0001": '1',
    "0010": '2',
    "0011": '3',
    "0100": '4',
    "0101": '5',
    "0110": '6',
    "0111": '7',
    "1000": '8',
    "1001": '9',
    "1010": 'a',
    "1011": 'b',
    "1100": 'c',
    "1101": 'd',
    "1110": 'e',
    "1111": 'f',
}

#mapping 4-4 bit block to above key value pairs
hexa = ''
for item in range(0,len(z),4):
    hexa += mapping[z[item:item+4]]

print(hexa)

if hexa == "746865206b696420646f6e277420706c6179":
    print(True)