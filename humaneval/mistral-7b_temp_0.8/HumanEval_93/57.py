
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    encoded = ""
    for letter in message:
        if letter == "a":
            encoded += "c"
        elif letter == "e":
            encoded += "f"
        elif letter == "i":
            encoded += "h"
        elif letter == "o":
            encoded += "j"
        elif letter == "u":
            encoded += "v"
        else:
            encoded += letter.swapcase()
    return encoded
