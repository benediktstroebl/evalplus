
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
    message = message.lower()
    lc = [x for x in message]
    vowels = ['a', 'e', 'i', 'o', 'u']
    i = 0
    for x in lc:
        if x in vowels:
            lc[i] = lc[i].upper()
        i += 1
    return ''.join(lc)

