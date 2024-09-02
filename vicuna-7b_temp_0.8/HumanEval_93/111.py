
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
    message = ''.join([c.upper() if c.isalpha() else c.lower() for c in message])
    message = ''.join([c.upper() if c.isalpha() else '0' + str(ord(c) - 1) if c.isalpha() else c for c in message])
    return message
