import csv
import requests
import json
from os import path
from hashlib import sha256
from keyboard import is_pressed

BREAK_KEY = 'esc'
FIELDS = ["String", "Valor Computado", "Número de zeros"]
WORD_API_URL = "https://api.dicionario-aberto.net/random"
HASHES_FILE_PATH = "hashes_from_strings.csv"
LOG_FILE_PATH =  "log.csv"
NUM_ZEROS_OF_KING = 43 # Current number of zeros found by the king
KEEP_WORDS_LOG = True # Keep a log of all words tested (the hashes_from_string only keep hashes bigger, in zeros, than the king)

lines_to_write = 64 # Number of hashes that hashes_from_string will have

if not path.exists(HASHES_FILE_PATH):
    with open(HASHES_FILE_PATH, "w", encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()

if KEEP_WORDS_LOG:
    if not path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'w', encoding='utf8') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()

def getWord():
    try:
        response = requests.get(WORD_API_URL)
        word = json.loads(response.text)['word']
        word = word.encode('ascii')
    except:
        word = ''
    return word

def countZeros(hash):
    count = 0

    for bit in list(hash):
        if bit == '0':
            count += 4
        elif bit == '1':
            count += 3
            return count
        elif bit in ['2', '3']:
            count += 2
            return count
        elif bit in ['4', '5', '6', '7']:
            count += 1
            return count
        else:
            return count

print('[SYSTEM]: The program is running...')
print(f'[SYSTEM]: Press {BREAK_KEY} to stop')
while lines_to_write > 0:
    word = getWord()

    if is_pressed(BREAK_KEY):
        break

    if word != '':
        computedHash = sha256(word).hexdigest()
        zeros = countZeros(computedHash)
        #print(word, computedHash, zeros)

        if KEEP_WORDS_LOG and zeros > 0:
            with open(LOG_FILE_PATH, 'a', encoding='utf8') as file:
                writer = csv.DictWriter(file, fieldnames=FIELDS)
                writer.writerow({
                    "String": word, 
                    "Valor Computado": computedHash, 
                    "Número de zeros": zeros
                })

        if zeros > NUM_ZEROS_OF_KING:
            with open(HASHES_FILE_PATH, 'a', encoding='utf8')  as file:
                writer = csv.DictWriter(file, fieldnames=FIELDS)
                writer.writerow({
                    "String": word, 
                    "Valor Computado": computedHash, 
                    "Número de zeros": zeros
                })
            lines_to_write -= 1
