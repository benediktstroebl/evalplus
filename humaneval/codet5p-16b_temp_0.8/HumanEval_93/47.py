
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

    
    if not message.isalpha():
        raise ValueError('The message must be only letters')
    
    m = [c.upper() if c.islower() else c.lower() for c in message]
    v = 'AEIOU'
    
    r = [c for c in m if c.isalpha()]
    for c in r:
        if c.lower() in v:
            r[r.index(c)] = m[v.index(c.lower()) + 2]
        else:
            r[r.index(c)] = m[v.index(c.lower()) + 1]
    
    return ''.join(r)
