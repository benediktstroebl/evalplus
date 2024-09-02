
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
    #return ''.join(['{}{}'.format(c.upper(), i) for c, i in zip(message, range(len(message)))]).lower()
    return ''.join(['{}{}'.format(c.upper(), i) for i, c in enumerate(message)]).lower()
