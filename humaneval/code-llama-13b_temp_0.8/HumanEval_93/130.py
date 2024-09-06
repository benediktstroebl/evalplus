
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
    for x in message:
        if x == "a":
            x = "C"
            return x
        elif x == "e":
            x = "G"
            return x
        elif x == "i":
            x = "K"
            return x
        elif x == "o":
            x = "S"
            return x
        elif x == "u":
            x = "T"
            return x
        elif x == "A":
            x = "C"
            return x
        elif x == "E":
            x = "G"
            return x
        elif x == "I":
            x = "K"
            return x
        elif x == "O":
            x = "S"
            return x
        elif x == "U":
            x = "T"
            return x
    return x
