import math
prime1 = 97
prime2 = 73
prime3 = 59

publickey = (prime1*prime2, prime3)



phi1 = prime1 - 1
phi2 = prime2 - 1

for i in range(1000000):
    ans = (i*prime3) % (phi1*phi2)
    if ans == 1:

        my_d = i
        break

privatekey = (prime1 * prime2, my_d)


# encryption

# input a string
ascii = []
print("Please Input a string")
string = input(str())
for j in range(len(string)):

    a = ord(string[j])
    ascii.append(a)


encryptedarray = []
for k in range (len(ascii)):

    secretoflife = ascii[k]
    raisedsecret = secretoflife**publickey[1] # raise secret num to power of second part of public key
    # divide answer from the raised secret by first part of public key and find the remainder, that is your encrypted number
    dividedraisedsecret = raisedsecret % publickey[0]
    encryptedarray.append(dividedraisedsecret)

encryptedmessage = ""
for encrypt in range (len(encryptedarray)):
    encryptedcharacter = chr(encryptedarray[encrypt])
    encryptedmessage+=encryptedcharacter # concat string

print(encryptedmessage)




# decryption


# decryption

# put the encrypted numbers in the encryptedarray
#encryptedarray = [4199, 2171, 2831, 1814, 6250, 2100, 5068, 4909, 128, 5032, 6025, 4435, 5068, 5345, 6025, 5068, 128, 4435, 5032, 128, 5345, 2171, 128, 2831, 2171, 4909, 5068, 128, 873, 680, 2171, 6250, 2100, 128, 6025, 2171, 2831, 1814, 6250, 2100, 5068, 4909, 5032, 128, 2100, 4677, 873, 5345, 128, 873, 5032, 2100, 4909, 2171, 5345, 2171, 2831, 780, 128, 4435, 5032, 128, 873, 680, 2171, 6250, 2100, 128, 2100, 5068, 968, 5068, 5032, 6025, 2171, 1814, 5068, 5032,465]
decryptedarray = [] # this array will store the decrypted values to be converted to character
for q in range(len(encryptedarray)):

    decrypt1 = encryptedarray[q]**privatekey[1]
    decrypt2 = decrypt1 % privatekey[0]
    decryptedarray.append(decrypt2)

decryptedmessage = ""
for r in range(len(decryptedarray)):
    decryptedcharacter = chr(decryptedarray[r])
    decryptedmessage+=decryptedcharacter


print(decryptedmessage)

