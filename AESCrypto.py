import base64
from Crypto.Cipher import AES
from Crypto import Random

class AESCrypto:
	def __init__(self, key):
		self.key = key
		self.BLOCK_SIZE = 16

    	def _pad(self, raw):
        	if (len(raw) % self.BLOCK_SIZE == 0):
        	    return raw
        	padding_required = self.BLOCK_SIZE - (len(raw) % self.BLOCK_SIZE)
        	padChar = b'\x00'
        	data = raw.encode('utf-8') + padding_required * padChar
        	return data
    
    	def _unpad(self, s):
        	s = s.rstrip(b'\x00')
		return s

	def encrypt(self, plainText):
        	if (plainText is None) or (len(plainText) == 0):
			raise ValueError('input text cannot be null or empty set')
		plainText = self._pad(plainText)
		iv = Random.new().read(AES.block_size)
		cipher = AES.new(self.key, AES.MODE_CBC, iv)
		return base64.b64encode(iv+cipher.encrypt(plainText))

	def decrypt(self, encryptedMessage):
		encryptedMessage = base64.b64decode(encryptedMessage)
		iv = encryptedMessage[:16]
		cipher = AES.new(self.key, AES.MODE_CBC, iv)
		return self._unpad(cipher.decrypt(encryptedMessage[:16]))
