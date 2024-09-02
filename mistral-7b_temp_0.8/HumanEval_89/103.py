
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

    # My Code:
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # result = ""
    # for i in range(0, len(s)):
    #     letter = s[i].lower()
    #     if letter not in alphabet:
    #         result += letter
    #     else:
    #         index = alphabet.find(letter)
    #         if index < 26 - 2:
    #             index += 2
    #         else:
    #             index = 2
    #         result += alphabet[index]
    # return result

    # SO Code:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    for i in range(len(s)):
        if s[i].islower():
            result += alphabet[(alphabet.index(s[i])+2) % 26]
        elif s[i].isupper():
            result += alphabet[(alphabet.index(s[i].lower())+
