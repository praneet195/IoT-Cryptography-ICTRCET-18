# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 16:15:59 2018

@author: psingh195
"""
import sys
import chilkat
import time
def twofish(i):
    crypt = chilkat.CkCrypt2()

    success = crypt.UnlockComponent("Anything for 30-day trial")
    if (success != True):
        print(crypt.lastErrorText())
        sys.exit()

#  Attention: use "blowfish2" for the algorithm name:
    crypt.put_CryptAlgorithm("twofish")

#  CipherMode may be "ecb", "cbc", or "cfb"
    crypt.put_CipherMode("cbc")

#  KeyLength (in bits) may be a number between 32 and 448.
#  128-bits is usually sufficient.  The KeyLength must be a
#  multiple of 8.
    crypt.put_KeyLength(128)

#  The padding scheme determines the contents of the bytes
#  that are added to pad the result to a multiple of the
#  encryption algorithm's block size.  Blowfish has a block
#  size of 8 bytes, so encrypted output is always
#  a multiple of 8.
    crypt.put_PaddingScheme(0)

#  EncodingMode specifies the encoding of the output for
#  encryption, and the input for decryption.
#  It may be "hex", "url", "base64", or "quoted-printable".
    crypt.put_EncodingMode("hex")

#  An initialization vector is required if using CBC or CFB modes.
#  ECB mode does not use an IV.
#  The length of the IV is equal to the algorithm's block size.
#  It is NOT equal to the length of the key.
    ivHex = "000102030405060708090A0B0C0D0E0F"
    crypt.SetEncodedIV(ivHex,"hex")

#  The secret key must equal the size of the key.  For
#  256-bit encryption, the binary secret key is 32 bytes.
#  For 128-bit encryption, the binary secret key is 16 bytes.
    keyHex = "000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F"
    crypt.SetEncodedKey(keyHex,"hex")
#  Encrypt a string...
#  The input string is 44 ANSI characters (i.e. 44 bytes), so
#  the output should be 48 bytes (a multiple of 8).
#  Because the output is a hex string, it should
#  be 96 characters long (2 chars per byte).
    encStr = crypt.encryptStringENC(i)

#  Now decrypt:
    decStr = crypt.decryptStringENC(encStr)
    return decStr

if __name__=="__main__":
    filenames=["string1mb.txt","string2mb.txt","string4mb.txt","string8mb.txt","string16mb.txt","string32mb.txt"]
    for i in filenames:
    	f=open(i,"r")
    	a=f.readline()
    	t0=time.clock()
    	if a==twofish(a):
         	print(time.clock()-t0)