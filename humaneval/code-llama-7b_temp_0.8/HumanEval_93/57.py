
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
    vowels = ['a','e','i','o','u']
    out = ''
    for c in message:
        if c.lower() in vowels:
            new_c = chr(ord(c.lower()) + 2)
            if c.isupper():
                new_c = new_c.upper()
            out += new_c
        else:
            new_c = c.lower() if c.isupper() else c.upper()
            out += new_c
    return out
