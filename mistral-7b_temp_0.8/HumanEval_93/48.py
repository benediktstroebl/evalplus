
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
    # TODO: insert your code here
    result = ""
    for letter in message:
        if letter.upper() == letter:
            result += letter.lower()
        elif letter.lower() == letter:
            result += letter.upper()
        elif letter == "e":
            result += "g"
        elif letter == "a":
            result += "c"
        elif letter == "o":
            result += "e"
        elif letter == "i":
            result += "h"
        elif letter == "u":
            result += "y"
        else:
            result += letter
    return result

