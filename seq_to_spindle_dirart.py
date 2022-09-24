#!/usr/bin/env python3
# dirart.seq to spindle textfile
import sys

try:
	fname = sys.argv[1]
	with open(fname) as fp:
		data = fp.read()
		data = data[1:]
except:
	print(f"usage: {sys.argv[0]} filename.seq [linelen=16]")
	sys.exit(1)

try:
	linelen = int(sys.argv[2])
except:
	linelen = 16  # dir art

i = 0
while i < len(data):
	print(data[i:i+linelen])# + f"{i}:{i+linelen}")
	i += linelen

