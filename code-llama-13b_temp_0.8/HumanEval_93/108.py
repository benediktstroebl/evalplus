
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
    vowels = 'aeiou'
    encoded = ''
    for c in message:
        if c.isupper():
            c = c.lower()
            if c in vowels:
                c = vowels[(vowels.index(c) + 2) % len(vowels)]
            c = c.upper()
        elif c in vowels:
            c = vowels[(vowels.index(c) + 2) % len(vowels)]
        encoded += c
    return encoded
    
    
