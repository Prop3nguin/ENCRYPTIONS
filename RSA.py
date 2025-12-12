from math import gcd
import random
PublicKey = 0
PrivateKey = []
# Key Generation --------------------------------------------------------
def keys():
  e = 0
  d = 0
  n = 0
  PossibleD = []
  while len(PossibleD) < 1:
    Primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    p = random.choice(Primes)
    q = p
    while q == p:
      q = random.choice(Primes)
    n = p * q  
    d = 0
    fi_N = (p - 1) * (q - 1)
    PossibleE = list(range(2, fi_N))
    Removed = 0
    for i in range(len(PossibleE)):
      if gcd(PossibleE[i - Removed], n) != 1:
        PossibleE.pop(i - Removed)
        Removed += 1
    Removed = 0
    for i in range(len(PossibleE)):
      if gcd(PossibleE[i - Removed], fi_N) != 1:
        PossibleE.pop(i - Removed)
        Removed += 1
    e = PossibleE[0]
    for i in range(len(Primes)):
      if (Primes[i] * e) % fi_N == 1 and Primes[i] != e:
        d = Primes[i]
        PossibleD.append(d)

  print("(" + str(e) + ", " + str(n) + ")")
  d = PossibleD[0]
  print("(" + str(d) + ", " + str(n) + ")")
# Encription ------------------------------------------------------------
def encrypt(PrivateKey):
  ABC = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  Message = list(input("Enter the message to encrypt: ").lower())
  EncryptedMessage = []
  TempList = []
  FinalMessage = []
  for i in range(len(Message)):
    try:
      EncryptedMessage.append(ABC.index(Message[i]) + 1)
    except ValueError:
      EncryptedMessage.append(Message[i])
  for i in EncryptedMessage:
    try:
      i = int(i)
      FinalMessage.append(i ** PrivateKey[0] % PrivateKey[1])
    except:
      FinalMessage.append(i)
  print(EncryptedMessage)
  return FinalMessage, PrivateKey
# Decryption ------------------------------------------------------------
def decrypt(PublicKey):
  ABC = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  print("Please put a ', ' in between every number. Omit brackets")
  MessageStr = input("Enter the message to decrypt: ")
  Message = MessageStr.split(", ")
  for i in range(len(Message)):
    try:
      num = int(Message[i])
      Message[i] = num
    except:
      if Message[i] == "' '" or Message[i] == '" "':
        Message[i] = ' '
      elif Message[i] == "','" or Message[i] == '","':
        Message[i] = ','
  DecryptedMessage = []
  d = PublicKey[0]
  n = PublicKey[1]
  for i in range(len(Message)):
    try:
      DecryptedMessage.append((Message[i] ** d) % n)
    except:
      DecryptedMessage.append(Message[i])
  LetterMessage = []
  try:
    for i in range(len(DecryptedMessage)):
      LetterMessage.append(ABC[DecryptedMessage[i] - 1])
    return "".join(map(str, LetterMessage))
  except IndexError:
    return ", ".join(map(str, DecryptedMessage)).upper()
# Actual Program loop. --------------------------------------------------
count = 0
print("_____________________RSA_Algorithm_____________________")
while True:
  if count == 3:
    count = 0
  if count == 0:
    print(" Would you like to...")
    print(" 1. Create a new key set?")
    print(" 2. Encrypt with a key set?")
    print(" 3. Decrypt with a key set?")
  UserInput = input(" Choice : ")
  if UserInput == "1":
    keys()
  elif UserInput == "2":
    while True:
      PrivateKey = []
      print("Private Key (#, #) ")
      First = input(" | Input the First Number of your private key : ")
      Second = input(" | Input the Second : ")
      try:
        PrivateKey.append(int(First))
        PrivateKey.append(int(Second))
        print(encrypt(PrivateKey))
        break
      except ValueError:
        print(" Incorrect Input, Value Error")
  elif UserInput == "3":
    while True:
      PublicKey = []
      print("Public Key (#, #) ")
      First = int(input(" | Input the First Number of your public key : "))
      Second = int(input(" | Input the Second : "))
      try:
        PublicKey.append(First)
        PublicKey.append(Second)
        print(PublicKey)
        print(decrypt(PublicKey))
        break
      except ValueError:
        print(" Incorrect Input, Value Error")
  count += 1
# Explanation -----------------------------------------------------------
# 1. Choose two Prime Numbers : p & q
# 2. Calculate N              : p*q = n
# 3. Calculate fi(N)          : fi(N) = (p-1)(q-1)
#             .
#             { 1 < e < fi(n) 
# 4. Choose e { Coprime with n & fi(n) 
#             { Private Key == (e, n) 
#
# 5. Choose d { de % fi(n) = 1
#             { Pulic Key == (d, n)
