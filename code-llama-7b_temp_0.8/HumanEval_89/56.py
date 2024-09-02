
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
    encrypted_message = ""
    for letter in s:
        if letter == " ":
            encrypted_message = encrypted_message + " "
        elif letter == "a":
            encrypted_message = encrypted_message + "d"
        elif letter == "b":
            encrypted_message = encrypted_message + "e"
        elif letter == "c":
            encrypted_message = encrypted_message + "f"
        elif letter == "d":
            encrypted_message = encrypted_message + "g"
        elif letter == "e":
            encrypted_message = encrypted_message + "h"
        elif letter == "f":
            encrypted_message = encrypted_message + "i"
        elif letter == "g":
            encrypted_message = encrypted_message + "j"
        elif letter == "h":
            encrypted_message = encrypted_message + "k"
        elif letter == "i":
            encrypted_message = encrypted_message + "l"
        elif letter == "j":
            encrypted_message = encrypted_message + "m"
        elif letter == "k":
            encrypted_message = encrypted_message + "n"
        elif letter == "l":
            encrypted_message = encrypted_message + "o"
        elif letter == "m":
            encrypted_message = encrypted_message + "p"
        elif letter == "n":
            encrypted_message = encrypted_message + "q"
        elif letter == "o":
            encrypted_message = encrypted_message + "r"
        elif letter == "p":
            encrypted_message = encrypted_message + "s"
        elif letter == "q":
            encrypted_message = encrypted_message + "t"
        elif letter == "r":
            encrypted_message = encrypted_message + "u"
        elif letter == "s":
            encrypted_message = encrypted_message + "v"
        elif letter == "t":
            encrypted_message = encrypted_message + "w"
        elif letter == "u":
            encrypted_message = encrypted_message + "x"
        elif letter == "v":
            encrypted_message = encrypted_message + "y"
        elif letter == "w":
            encrypted_message = encrypted_message +
