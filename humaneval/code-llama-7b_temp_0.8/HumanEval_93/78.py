
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
    message = message.replace(' ','')
    enc = message.swapcase()
    for v in 'aeiou':
        i = 2
        while v in enc:
            enc = enc.replace(v, enc[enc.find(v)+i])
            i += 2
    return enc

