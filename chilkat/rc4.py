    # -*- coding: utf-8 -*-


import sys
import chilkat
import time

def rc4chilkat(i):
    crypt = chilkat.CkCrypt2()

    success = crypt.UnlockComponent("Anything for 30-day trial")
    if (success != True):
        print("Crypt component unlock failed")
        sys.exit()

    #  Set the encryption algorithm = "arc4"
    crypt.put_CryptAlgorithm("arc4")

    #  KeyLength may range from 1 byte to 256 bytes.
    #  (i.e. 8 bits to 2048 bits)
    #  ARC4 key sizes are typically in the range of
    #  40 to 128 bits.
    #  The KeyLength property is specified in bits:
    crypt.put_KeyLength(128)

    #  Note: The PaddingScheme and CipherMode properties
    #  do not apply w/ ARC4.  ARC4 does not encrypt in blocks --
    #  it is a streaming encryption algorithm. The number of output bytes
    #  is exactly equal to the number of input bytes.

    #  EncodingMode specifies the encoding of the output for
    #  encryption, and the input for decryption.
    #  It may be "hex", "url", "base64", or "quoted-printable".
    crypt.put_EncodingMode("hex")

    #  Note: ARC4 does not utilize initialization vectors.  IV's only
    #  apply to block encryption algorithms.

    #  The secret key must equal the size of the key.
    #  For 128-bit encryption, the binary secret key is 16 bytes.
    keyHex = "000102030405060708090A0B0C0D0E0F"
    crypt.SetEncodedKey(keyHex,"hex")
    #  Encrypt a string...
    #  The output length is exactly equal to the input.  In this
    #  example, the input string is 44 chars (ANSI bytes) so the
    #  output is 44 bytes -- and when hex encoded results in an
    #  88-char string (2 chars per byte for the hex encoding).
    encStr = crypt.encryptStringENC(i)


    #  Now decrypt:
    decStr = crypt.decryptStringENC(encStr)
    return decStr
if __name__=="__main__":
    filee=open("string64mb.txt","r")
    a=filee.readline()
    n=len(a)//2
    t0=time.clock()
    if a[:n]==rc4chilkat(a[:n]) and a[n:]==rc4chilkat(a[n:]):
        print(time.clock()-t0)
