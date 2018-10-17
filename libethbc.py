import sha3
import binascii
from ecdsa import SigningKey, SECP256k1
import urllib.request
import re

class RTM :
	def menu():
		print("Type 1 ===> START BRUTE FORCE WITH A POWER OF 2 AND END IT WITH ANOTHER POWER OF TWO")
		print("Type 2 ===> START BRUTE FORCE WITH A RANDOM NUMBER FROM POWER OF 2^X AND END IT WITH POWER OF 2^(X+Y)")
		print("Type 3 ===> START BRUTE FORCE WITH A SPECIFIC PRIVATE KEY AND END IT WITH SPECIFIC PRIVATE KEY")

class eth_check :
	@staticmethod
	def build_url(account , account2 , account3, account4, account5, account6, account7, account8, account9, account10):
		url = 'https://api.etherscan.io/api?module=account&action=balancemulti&address=%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (account , account2 , account3, account4, account5, account6, account7, account8, account9, account10)
		#print(url)
		return url
	@staticmethod
	def get_balance(url):
		try:
			headers = {}
			headers[
				'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
			req = urllib.request.Request(url, headers=headers)
			resp = urllib.request.urlopen(req)
			respdata = str(resp.read())
			paragraphs = re.findall(r'"(\d*)"', respdata)
			str1 = "".join(paragraphs)
			return str1
		except AttributeError :
			import time
			time.sleep(5)
			print("TOO MANY REQ / 5 SEC TIME OUT")
			return -1
		except TimeoutError :
			import time
			time.sleep(12)
			print("WEB SITE NOT RESPOND DUE TO MANY REQ / 15 SEC TIME OUT")
			return -1
	@staticmethod	
	def save_eth_address(num, private, public, value):
		with open("fethcdata.txt", "a") as mimix:
			mimix.writelines(str(num))
			mimix.writelines(" , ")
			mimix.writelines(private)
			mimix.writelines(" , ")
			mimix.writelines(public)
			mimix.writelines(" , ")
			mimix.writelines(value)
			mimix.write("\n")
	@staticmethod	
	def com(comp):
		command = '{:064x}'.format(comp)
		return command
	@staticmethod	
	def start(startpoint , endpoint):
		for x in range(startpoint,endpoint, 10) :
			command = eth_check.com(x)
			command2 = '{:064x}'.format(x+1)
			command3 = eth_check.com(x+2)
			command4 = eth_check.com(x+4)
			command5 = eth_check.com(x+5)
			command6 = eth_check.com(x+6)
			command7 = eth_check.com(x+7)
			command8 = eth_check.com(x+8)
			command9 = eth_check.com(x+9)
			command10 = eth_check.com(x+10)
			private = binascii.unhexlify(command)
			private2 = binascii.unhexlify(command2)
			private3 = binascii.unhexlify(command3)
			private4 = binascii.unhexlify(command3)
			private5 = binascii.unhexlify(command3)
			private6 = binascii.unhexlify(command3)
			private7 = binascii.unhexlify(command3)
			private8 = binascii.unhexlify(command3)
			private9 = binascii.unhexlify(command3)
			private10 = binascii.unhexlify(command3)			   
			keccak = sha3.sha3_256()
			keccak2 = sha3.sha3_256()
			keccak3 = sha3.keccak_256()
			keccak4 = sha3.keccak_256()
			keccak5 = sha3.keccak_256()
			keccak6 = sha3.keccak_256()
			keccak7 = sha3.keccak_256()
			keccak8 = sha3.keccak_256()
			keccak9 = sha3.keccak_256()
			keccak10 = sha3.keccak_256()

			keccak.update(SigningKey.from_string(private, curve=SECP256k1).get_verifying_key().to_string())
			keccak2.update(SigningKey.from_string(private2, curve=SECP256k1).get_verifying_key().to_string())
			keccak3.update(SigningKey.from_string(private3, curve=SECP256k1).get_verifying_key().to_string())
			keccak4.update(SigningKey.from_string(private4, curve=SECP256k1).get_verifying_key().to_string())
			keccak5.update(SigningKey.from_string(private5, curve=SECP256k1).get_verifying_key().to_string())
			keccak6.update(SigningKey.from_string(private6, curve=SECP256k1).get_verifying_key().to_string())
			keccak7.update(SigningKey.from_string(private7, curve=SECP256k1).get_verifying_key().to_string())
			keccak8.update(SigningKey.from_string(private8, curve=SECP256k1).get_verifying_key().to_string())
			keccak9.update(SigningKey.from_string(private9, curve=SECP256k1).get_verifying_key().to_string())
			keccak10.update(SigningKey.from_string(private10, curve=SECP256k1).get_verifying_key().to_string())

			address = "0x{0}".format(keccak.hexdigest()[24:])
			address2 = "0x{0}".format(keccak2.hexdigest()[24:])
			address3 = "0x{0}".format(keccak3.hexdigest()[24:])
			address4 = "0x{0}".format(keccak4.hexdigest()[24:])
			address5 = "0x{0}".format(keccak5.hexdigest()[24:])
			address6 = "0x{0}".format(keccak6.hexdigest()[24:])
			address7 = "0x{0}".format(keccak7.hexdigest()[24:])
			address8 = "0x{0}".format(keccak8.hexdigest()[24:])
			address9 = "0x{0}".format(keccak9.hexdigest()[24:])
			address10 = "0x{0}".format(keccak10.hexdigest()[24:])

			value = eth_check.get_balance(eth_check.build_url(address , address2 , address3 , address4, address5, address6, address7, address8, address9, address10))
			if float(value) == -1:
				x=x-1
			if float(value) > 10000000000:
				eth_check.save_eth_address(x, command, address, value)
				eth_check.save_eth_address(x+1, command2, address2, value)
				eth_check.save_eth_address(x+2, command3, address2, value)
				eth_check.save_eth_address(x+4, command4, address, value)
				eth_check.save_eth_address(x+5, command5, address2, value)
				eth_check.save_eth_address(x+6, command6, address2, value)
				eth_check.save_eth_address(x+7, command7, address, value)
				eth_check.save_eth_address(x+8, command8, address2, value)
				eth_check.save_eth_address(x+9, command9, address2, value)
				eth_check.save_eth_address(x+10, command10, address, value)
				print("==========================================")
				print("PV:" , command)
				print("PV:" , command2)
				print("PV:" , command3)
				print("PV:" , command4)
				print("PV:" , command5)
				print("PV:" , command6)
				print("PV:" , command7)
				print("PV:" , command8)
				print("PV:" , command9)
				print("PV:" , command10)
				print("CHECK THE VALL")
				print("==========================================")
			else :
				print(command , "CHECKED")
				print(command2 , "CHECKED")
				print(command3 , "CHECKED")
				print(command4 , "CHECKED")
				print(command5 , "CHECKED")
				print(command6 , "CHECKED")
				print(command7 , "CHECKED")
				print(command8 , "CHECKED")
				print(command9 , "CHECKED")
				print(command10 , "CHECKED")
	@staticmethod	
	def random_start(startpoint , endpoint):
		from random import randint
		randstart = randint(2**startpoint , 2**endpoint)
		print (randstart)
		return randstart

	