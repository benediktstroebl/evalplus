
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
    char_to_int = ord('a')
    int_to_int = ord('a')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = alphabet[::2]
    new_alphabet2 = alphabet[1::2]
    new_alphabet = new_alphabet2 + new_alphabet
    # print(new_alphabet)
    new_alphabet = new_alphabet[::-1]
    # print(new_alphabet)
    for index, char in enumerate(alphabet):
        char_to_int = ord(char)
        int_to_int = ord(alphabet[index])
        # print(char_to_int, int_to_int)
        new_alphabet[index] = chr(char_to_int -1)
        new_alphabet[index] = chr(int_to_int -1)
    # print(new_alphabet)
    # for char in new_alphabet:
    #     print(char)
    # print("new alphabet", new_alphabet)
    s = s.lower()
    new_s = ''
    for char in s:
        if char == ' ':
            new_s += ' '
            continue
        for index2, char2 in enumerate(new_alphabet):
            if char == char2:
                new_s += new_alphabet[index2]
                break
    return new_s
    
    