a, b = 0, 1
n = 0
while n<1000000:
    print a
    c = a
    b += a
    a = c
    n += 1
print "Decrypted successfully"
