#!/usr/bin/python
# Author : Linggar Primahastoko
# July 2011

import itertools
import sys
import hashlib

howto = '\nUsage :\n\
./md5brute.py combinedChars[a,A,n,an,An,aAn] maxlength HashToCrack\n\n\
about the combinedChars:\n\
a = lowercase\n\
A = uppercase\n\
n = numeric\n\
an = lowercase + numeric\n\
An = uppercase + numeric\n\
aAn = lowercase + uppercase + numeric\n\n\
example : ./md5brute.py a 5 21232f297a57a5a743894a0e4a801fc3\n'

chars0 = 'abcdefghijklmnopqrstuvwxyz'
chars1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars2 = '1234567890'
chars3 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
chars4 = 'abcdefghijklmnopqrstuvwxyz1234567890'
chars5 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
chars6 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def brute():
	length = int(sys.argv[2]) + 1

	if sys.argv[1] == 'a':
		final = chars0
	elif sys.argv[1] == 'A':
		final = chars1
	elif sys.argv[1] == 'n':
		final = chars2
	elif sys.argv[1] == 'aA':
        	final = chars3
	elif sys.argv[1] == 'an':
        	final = chars4
	elif sys.argv[1] == 'An':
        	final = chars5
	elif sys.argv[1] == 'aAn':
        	final = chars6

	for i in range(1,length):
		for p in itertools.permutations(final, i):
			crack = ''.join(p)
			m = hashlib.md5()
			m.update(crack)
			if m.hexdigest() != sys.argv[3]:
				print crack,"is not the password"
			else:
				print crack,"is it!"
				sys.exit()

def main():
	if len(sys.argv) <=1:
	        print howto
                sys.exit(1)
        else:
                brute()

if __name__ == "__main__" :
        main()
