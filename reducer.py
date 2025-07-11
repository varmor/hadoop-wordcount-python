#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

# Process each line from mapper output
for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)

    if word == current_word:
        current_count += count
    else:
        if current_word is not None:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Output the final word count
if current_word == word:
    print(f"{current_word}\t{current_count}")

