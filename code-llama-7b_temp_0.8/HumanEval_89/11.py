
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
            encrypted_message += " "
        elif letter == "a":
            encrypted_message += "m"
        elif letter == "b":
            encrypted_message += "n"
        elif letter == "c":
            encrypted_message += "o"
        elif letter == "d":
            encrypted_message += "p"
        elif letter == "e":
            encrypted_message += "q"
        elif letter == "f":
            encrypted_message += "r"
        elif letter == "g":
            encrypted_message += "s"
        elif letter == "h":
            encrypted_message += "t"
        elif letter == "i":
            encrypted_message += "u"
        elif letter == "j":
            encrypted_message += "v"
        elif letter == "k":
            encrypted_message += "w"
        elif letter == "l":
            encrypted_message += "x"
        elif letter == "m":
            encrypted_message += "y"
        elif letter == "n":
            encrypted_message += "z"
        elif letter == "o":
            encrypted_message += "a"
        elif letter == "p":
            encrypted_message += "b"
        elif letter == "q":
            encrypted_message += "c"
        elif letter == "r":
            encrypted_message += "d"
        elif letter == "s":
            encrypted_message += "e"
        elif letter == "t":
            encrypted_message += "f"
        elif letter == "u":
            encrypted_message += "g"
        elif letter == "v":
            encrypted_message += "h"
        elif letter == "w":
            encrypted_message += "i"
        elif letter == "x":
            encrypted_message += "j"
        elif letter == "y":
            encrypted_message += "k"
        elif letter == "z":
            encrypted_message += "l"
        else:
            encrypted_message += " "
    return encrypted_message
