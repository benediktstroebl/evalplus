
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    start = ord('a')
    end = ord('z') + 1
    alpha = [chr(x) for x in range(start, end)]
    num_letters = len(s)
    start_num = ord(s[0]) - ord('a')
    end_num = ord(s[num_letters - 1]) - ord('a')
    shift_num = start_num + end_num + 2
    print(shift_num)
    encrypt_alphabet = list(alpha)
    encrypt_alphabet.sort()
    encrypted_letters = ''
    for letter in s:
        if letter.islower():
            encrypted_letters += encrypt_alphabet[shift_num][:1]
        else:
            encrypted_letters += encrypt_alphabet[shift_num][:1].upper()
        shift_num += 1
    if shift_num % 26 == 0:
        shift_num = 0
    return encrypted_letters
