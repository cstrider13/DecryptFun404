#!/usr/bin/env python
import cryptBreak
from cryptBreak import *
from BitVector import *
is_done = 0
num = 16765#0
while(is_done == 0 & num < 65535):
	someRandomInteger = num#9999 #Arbitrary integer for creating a BitVector
	key_bv = BitVector(intVal=someRandomInteger, size=16)
	decryptedMessage = cryptBreak('encrypted.txt', key_bv)
	#print("decryptedMessage = ", decryptedMessage)
	if ('Mark Twain' in decryptedMessage):
		print('Encryption Broken!')
		is_done = 1
	else:
		print('Not decrypted yet')
	num += 1
	print(num)
