
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
    message = "".join(sorted(message))
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded = ""
    for i in range(len(message)):
        c = message[i]
        if c.isalpha() and c.isupper():
            c = c.isalpha() and c.islower() or c.isupper()
        encoded += alphabet[int(c) + 32]
    return encoded
