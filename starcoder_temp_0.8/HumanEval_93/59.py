
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
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    vowels = "AEIOU"

    new_message = ""
    for c in message:
        if c.upper() in vowels:
            new_message += alphabet[vowels.index(c.upper()) + 2]
        elif c.upper() not in vowels:
            new_message += c
    return new_message

