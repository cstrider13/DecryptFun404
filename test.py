
# coding: utf-8

# In[6]:

#import cryptBreak
from cryptBreak.py import *
from BitVector import *
someRandomInteger = 9999 #Arbitrary integer for creating a BitVector
key_bv = BitVector(intVal=someRandomInteger, size=16)
decryptedMessage = cryptBreak.cryptBreak('encrypted.txt', key_bv)
if 'Mark Twain' in decryptedMessage:
    print('Encryption Broken!')
else:
    print('Not decrypted yet')


# In[ ]:



