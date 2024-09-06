
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
    res = ''
    for c in message:
        if c == 'a':
            res += 'c'
        elif c == 'e':
            res += 'g'
        elif c == 'i':
            res += 'k'
        elif c == 'o':
            res += 'q'
        elif c == 'u':
            res += 'w'
        else:
            res += c.upper()
    return res


