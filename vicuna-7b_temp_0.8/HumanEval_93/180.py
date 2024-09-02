
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
    # check if message is a string and only contains letters
    if not isinstance(message, str) or not all(c.isalnum() for c in message):
        raise ValueError('message should be a string containing only letters')
    
    # swap case of all letters
    message = message.upper()
    
    # replace all vowels with a letter 2 places ahead in alphabet
    message = message.replace('a', 'b')
    message = message.replace('b', 'd')
    message = message.replace('c', 'd')
    message = message.replace('d', 'e')
    message = message.replace('e', 'f')
    message = message.replace('f', 'g')
    message = message.replace('g', 'h')
    message = message.replace('h', 'i')
    message = message.replace('i', 'j')
    message = message.replace('j', 'k')
    message = message.replace('k', 'l')
    message = message.replace('l', 'm')
    message = message.replace('m', 'n')
    message = message.replace('o', 'p')
    message = message.replace('p', 'q')
    message = message.replace('q', 'r')
    message = message.replace('r', 's')
    message = message.replace('s', 't')
    message = message.replace('t', 'u')
    message = message.replace('u', 'v')
    message = message.replace('v', 'w')
    message = message.replace('w', 'x')
    message = message.replace('x', 'y')
    message = message.replace('y', 'z')
    message = message.replace('z', 'a')
    
    return message