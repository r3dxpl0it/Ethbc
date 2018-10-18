'''
_______________________________________________________________________
|[] R3DXPL0IT SHELL                                            |ROOT]|!"|
|"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""|"| 
|CODED BY > R3DXPLOIT(JIMMY)                                          | |
|EMAIL > RETURN_ROOT@PROTONMAIL.COM                                   | |
|GITHUB > https://github.com/r3dxpl0it                                | |
|WEB-PAGE > https://r3dxpl0it.Github.io                               |_|
|_____________________________________________________________________|/|
'''
import libethbc
pyt.RTM.menu()
counttype = input("GIVE THE FUNCTION A VALUE :) >>>")
if counttype == "2":
   inputstart = input("type a number to start from from 1 to 254 \t >>>")
   inputend = input("type a number from STARTPOINT to 254 \t\t >>>")
   genrand = pyt.eth_check.random_start(int(inputstart), int(inputend))
   for x in range(int(inputstart), int(inputend)):
	   startpoint = genrand
	   endpoint = 2 ** (x + 1)
	   filename = "fetchfile.txt"
	   pyt.eth_check.start(startpoint , endpoint)
if counttype == "1":
   inputstart = input("type a number to start from from 1 to 254 \t >>>")
   inputend = input("type a number from STARTPOINT to 254 \t\t >>>")
   for x in range(int(inputstart), int(inputend)):
	   startpoint = 2 ** x
	   endpoint = 2 ** (x + 1)
	   filename = "fetchfile.txt"
	   pyt.eth_check.start(startpoint, endpoint)
	   # print("2 TO THE POWER OF " , x+1 , " , SUCCESS!")
if counttype == "3":
   inputstart = input("type a private key (converted to int) to start \t >>>")
   inputend = input("type a a private key (converted to int) greater than " ,inputstart ,"\t\t >>>")
   pyt.eth_check.start(int(inputstart), int(inputend))
