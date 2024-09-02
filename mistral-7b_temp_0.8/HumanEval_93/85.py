
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
    vowels = "aeiou"
    out = ""
    for c in message:
        if c.isalpha():
            if c.lower() in vowels:
                out += chr(ord(c) + 2)
            elif c.isupper():
                out += chr(ord(c) + 32)
            else:
                out += chr(ord(c) - 32)
        else:
            out += c
    return out


