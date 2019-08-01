def increase_char(ch, n):
    return chr((ord(ch)+n)%256)
def decrease_char(ch,n):
    return chr((ord(ch)+(256-n))%256)

x = "Hello"
enc = ""
dec = ""
for i in x:
    enc = enc+increase_char(i,40)
print(enc)
for i in enc:
    dec = dec+decrease_char(i,40)
print(dec)