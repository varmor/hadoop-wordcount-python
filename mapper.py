#!/usr/bin/env python3
import sys

# Read each line from standard input
for line in sys.stdin:
    line = line.strip()  
    words = line.split()  
    for word in words:
        print(f"{word}\t1") 

