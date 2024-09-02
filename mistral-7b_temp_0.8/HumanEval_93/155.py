
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
    map_vowels = {
        'A': 'C',
        'E': 'G',
        'I': 'K',
        'O': 'Q',
        'U': 'X'
    }
    l = []
    for c in message:
        if c.upper() in vowels:
            l.append(map_vowels[c.upper()])
        else:
            l.append(c.swapcase())
    return ''.join(l)
