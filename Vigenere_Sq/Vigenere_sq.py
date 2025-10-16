from email import header

from pyexpat.errors import messages

alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ '
alpha_len = len(alphabet)

def pretty_print(vsq: list):
    for i, row in enumerate(vsq):
        print( f" |{' | '.join(row)} |")
        if i == 0:
            suffix = '---|' * (alpha_len + 1)
            print(f'|{suffix}')




def print_header():
    header = [' ']
    #print(f'|   |', end='')
    for a in alphabet:
        #print(f' {a} |', end='')
        header.append(a)
    #print()
    #suffix = '---|' * (alpha_len + 1)
    #print(f'|{suffix}')
    return header


def print_row (a:int):
    row = []
    for i, letter in enumerate(alphabet):
        row.append(alphabet[(i + a) % alpha_len])
        #print(f' {alphabet[(i + a) % alpha_len]} |', end='')
    #print()
    return row


def vigenere_sq(alphabet):
    sq = []
    header = print_header()
    sq.append(header)
    for shift in range(alpha_len):
        #print('|', end='')
        row = print_row(shift)
        row.insert(0, alphabet[shift])
        sq.append(row)
        #print(row)
        #print()
    return sq

pretty_print(vigenere_sq(alphabet))

def letter_to_index(letter:str, alphanet:str) -> int:
    for i, c in  enumerate(alphanet):
        if letter == c:
            return i

    return -1

def index_to_letter(index:int, alphanet:str):
   if 0 <= index < alpha_len:
       return alphanet[index]
   return None

def vigenere_index(key_letter, plaintext_letter, alphabet):
    ci = ((letter_to_index(key_letter,alphabet) +
           letter_to_index(plaintext_letter, alphabet)) % alpha_len)
    print(ci)
    return index_to_letter(ci, alphabet)


def undo_vignere_index(key_letter:str, cipher_letter:str, alphabet:str) -> str:
    # Pi = ( C - K) % AL
    pi = ((letter_to_index(cipher_letter, alphabet) -
           letter_to_index(key_letter, alphabet)) % alpha_len)
    return index_to_letter(pi, alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = []
    for i, pt in enumerate(plaintext):
        cipher_text.append(
            vigenere_index(key[i%len(key)], pt, alphabet)
        )
    return ''.join(cipher_text)

def dencrypt_vigenere(key, ciphertext, alphabet):
    plain_text = []
    for i, ct in enumerate(ciphertext):
        #print(i, ct, key [i%len(key)])
        plain_text.append(
            undo_vignere_index(key[i%len(key)], ct, alphabet)
        )
    return ''.join(plain_text)



#vigenere_sq()
#print(index_to_letter(alphabet[27, alphabet))
key = 'DAVINCI'
#plain_text = 'THE EAGLE HAS LANDED'
# print(letter_to_index('T', alphabet))
#print(vigenere_index('D', 'T', alphabet))
#encrypt_vigenere(key, plain_text, alphabet)
#et = encrypt_vigenere(key, plain_text, alphabet)
#pt = dencrypt_vigenere(key, et, alphabet)
#print(et, pt)



choice = 0
et_list = []
while choice != 4:
    choice = int(input("Enter your choice [1, 2, 3]:")),
    if  not (1 <= choice <= 3):
        continue
    if choice == 1:
        message = input("what is you message: ")
    et_list.append(encrypt_vigenere(key, message, alphabet))
    if choice == 2:
        for ct in et_list:
             if choice == 3:
                for ct in et_list:
                 print(ct)
                print('performing')







