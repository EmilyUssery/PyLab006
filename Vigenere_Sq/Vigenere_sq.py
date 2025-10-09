
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_len = len(alphabet)

def print_header():
    print(f'|   |', end='')
    for a in alphabet:
        print(f' {a} |', end='')
    print()
    suffix = '---|' * (alpha_len + 1)
    print(f'|{suffix}')

def vigenere_sq(alphabet):
    print_header()
    for shift in range(alpha_len):
        print('|', end='')
        for i, letter in enumerate(alphabet):
            print(f' {alphabet[(i + shift) % alpha_len]} |', end='')
        print()

vigenere_sq(alphabet)

def letter_to_index(letter:str, alphanet:str) -> int:
    for i, c in  enumerate(alphanet):
        if letter == c:
            return i

    return -1

def index_to_letter(index:int, alphanet:str):
   if 0 <= index < 26:
       return alphanet[index]
   return None

def vigenere_index(key_letter, plaintext_letter, alphabet):
    ci = ((letter_to_index(key_letter,alphabet) +
           letter_to_index(plaintext_letter, alphabet)) % alpha_len)
    print(ci)
    return index_to_letter(ci, alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    for i, pt in enumerate(plaintext):
        #print(i, pt, key [i%len(key)])
        cipher_text += vigenere_index(key[i%len(key)], pt, alphabet)

    return cipher_text





#vigenere_sq()
#print(index_to_letter(alphabet[27, alphabet))
key = 'DAVINCI'
plain_text = 'THE EAGLE HAS LANDED'
# print(letter_to_index('T', alphabet))
#print(vigenere_index('D', 'T', alphabet))
#encrypt_vigenere(key, plain_text, alphabet)
print(encrypt_vigenere(key, plain_text, alphabet))