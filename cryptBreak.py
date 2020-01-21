#!/usr/bin/env python
import os
#import subprocess
from subprocess import *
import pexpect
#Arguments:
# ciphertextFile: String containing file name of the ciphertext (e.g. encrypted.txt )
# key_bv: 16-bit BitVector of the key used to try to decrypt the ciphertext.
#Function Description:
# Attempts to decrypt ciphertext contained in ciphertextFile using key_bv and returns
#  the original plaintext as a string
def cryptBreak(ciphertextFile,key_bv):
    #DecryptForFun.py ciphertextFile output.txt
    #exec('DecryptForFun.py ciphertextFile output.txt')
	#os.system("DecryptForFun.py encrypted.txt output.txt")
	#child = pexpect.spawn('python DecryptForFun.py encrypted.txt output.txt')
	#child.expect("\nEnter key: ")
	#child.sendline(key_bv)
	test_str = str(key_bv)
	child = Popen(['python', 'DecryptForFun.py', 'encrypted.txt', 'output.txt'], stdin=PIPE)
	child.communicate(test_str)#key_bv)
	FILEIN = open('output.txt', 'r')
	contents = FILEIN.read()
	FILEIN.close()
	return contents
	

#from BitVector import*
#someRandomInteger = 9999
#key_bv = BitVector(intVal=someRandomInteger, size=16)
#decryptedMessage = cryptBreak('encrypted.txt', key_bv)
#if 'Mark Twain' in decryptedMessage:
#	print('Encryption Broken!')
#else:
#	print('Not decrypted yet')
