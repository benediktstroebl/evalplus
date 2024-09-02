
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
    vowels = 'AEIOU'
    vowels2 = 'BFCST'
    encoded = ''
    
    for c in message:
        if c.isupper():
            # Uppercase
            if c in vowels:
                encoded += vowels2[vowels.index(c)]
            else:
                encoded += c.lower()
        else:
            # Lowercase
            if c in vowels:
                encoded += vowels2[vowels.index(c.upper())]
            else:
                encoded += c
            
    return encoded

