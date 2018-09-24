# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:55:18 2018

@author: psingh195
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:55:18 2018

@author: psingh195
"""
import sys
import chilkat
import time

def des3chilkat(i):
    crypt = chilkat.CkCrypt2()

    success = crypt.UnlockComponent("Anything for 30-day trial")
    if (success != True):
        print(crypt.lastErrorText())
        sys.exit()

    #  Specify 3DES for the encryption algorithm:
    crypt.put_CryptAlgorithm("3des")

    #  CipherMode may be "ecb" or "cbc"
    crypt.put_CipherMode("cbc")

    #  KeyLength must be 192.  3DES is technically 168-bits;
    #  the most-significant bit of each key byte is a parity bit,
    #  so we must indicate a KeyLength of 192, which includes
    #  the parity bits.
    crypt.put_KeyLength(192)

    #  The padding scheme determines the contents of the bytes
    #  that are added to pad the result to a multiple of the
    #  encryption algorithm's block size.  3DES has a block
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
    ivHex = "0001020304050607"
    crypt.SetEncodedIV(ivHex,"hex")

    #  The secret key must equal the size of the key.  For
    #  3DES, the key must be 24 bytes (i.e. 192-bits).
    keyHex = "000102030405060708090A0B0C0D0E0F0001020304050607"
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
    	if a==des3chilkat(a):
         	print(time.clock()-t0)