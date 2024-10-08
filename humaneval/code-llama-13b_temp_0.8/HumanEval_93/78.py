
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
    vowels = 'aeiouAEIOU'
    message = list(message)
    for i, c in enumerate(message):
        if c.lower() in vowels:
            message[i] = vowels[(vowels.index(c.lower()) + 2) % len(vowels)]
        message[i] = c.lower() if c.isupper() else c.upper()
    return ''.join(message)
