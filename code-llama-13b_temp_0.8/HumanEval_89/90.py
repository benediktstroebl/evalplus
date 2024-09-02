
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
    # your code

    # new_string = s[2:] + s[:2]
    # return new_string
    #
    # Tip:
    # You can iterate through a string like a list:
    # string[0] returns the first letter of the string
    # string[1] returns the second letter of the string
    # string[2] returns the third letter of the string
    #
    # You can add strings together like so:
    # string1 + string2 returns the string "string1string2"
    #
    # You can subtract strings from each other:
    # string1 - string2 returns the letters in string1 that
    # are not in string2

    #
    # ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    #
    # def encrypt(s):
    #     encrypted_string = ""
    #     for letter in s:
    #         if letter.lower() in ALPHABET:
    #             position = ALPHABET.find(letter.lower())
    #             shifted_letter = ALPHABET[position+2]
    #             if letter.isupper():
    #                 encrypted_string += shifted_letter.upper()
    #             else:
    #                 encrypted_string += shifted_letter
    #         else:
    #             encrypted_string += letter
    #     return encrypted_string
    #
    # print(encrypt("hi"))
    #
    # print(encrypt("asdfghjkl"))
    #
    # print(encrypt("gf"))
    #
    # print(encrypt("et"))

    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    encrypted_string = ""

    for letter in s:
        if letter.lower() in ALPHABET:
            position = ALPHABET.find(letter.lower())
            shifted_letter = ALPHABET[position+2]
            if letter.isupper():
                encrypted_string += shifted_letter.upper()
            else:
                encrypted_string += shift
