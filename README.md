# Crypto Class Hashgame
 
An simple script to compute the hash of a random word from Brazilian dictionary to get a hash that initiates with most zeros than the current king count.

Words get with [Dictionary API](https://api.dicionario-aberto.net).

# Files

- hashes_from_strings.csv
    This file keep all the hashes with more zeros than the king, storing:
    1. The string that give this value
    1. The value in hexadecimal
    1. The number of zeros

- log.csv
    This file is optional, in main.py turn KEEP_WORDS_LOG to False to disable it, and keep all the words tested that result in a hashe with at least one zero. Stores the same information from hashes_from_strings.csv.
---
# :D