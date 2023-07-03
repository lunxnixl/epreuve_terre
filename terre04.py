#!/usr/bin/python

import sys

lettre = sys.argv[1]

start_letter = lettre
end_letter = 'z'

while lettre <= end_letter:
    print(lettre, end='')
    lettre = chr(ord(lettre) + 1)

