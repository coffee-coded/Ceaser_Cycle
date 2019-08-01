def encryption(ch, n):
    return chr((ord(ch) + n) % 256)


def decryption(ch, n):
    return chr((ord(ch) + (256 - n)) % 256)


x = input("Enter text to be encrypted : ")
n = input("Enter the shift integer to be used : ")
enc = ""
dec = ""
print("Encrypted")
for i in x:
    enc = enc + encryption(i, 40)
print("Encrypted message : ", enc)
print("Decrypted")
for i in enc:
    dec = dec + decryption(i, 40)
print("Decrypted message : ", dec)
