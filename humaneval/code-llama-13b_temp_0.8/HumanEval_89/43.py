
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
    temp = s.split()
    vowels = ['a','e','i','o','u']
    for index, word in enumerate(temp):
        new_word = ''
        for letter in word:
            if letter.lower() in vowels:
                if letter.isupper():
                    new_word += chr(ord(letter) + 2)
                else:
                    new_word += chr(ord(letter) + 2).upper()
            elif letter.lower() == 'y':
                if letter.isupper():
                    new_word += 'A'
                else:
                    new_word += 'a'
            else:
                if letter.isupper():
                    new_word += chr(ord(letter) + 2 - 26)
                else:
                    new_word += chr(ord(letter) + 2 - 26).upper()
        temp[index] = new_word
    return ' '.join(temp)
