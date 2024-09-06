
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
    message = message.replace('a', 'z')
    message = message.replace('e', 'z')
    message = message.replace('i', 'y')
    message = message.replace('o', 'u')
    message = message.replace('u', 'w')
    message = message.replace('A', 'Z')
    message = message.replace('E', 'Y')
    message = message.replace('I', 'B')
    message = message.replace('O', 'V')
    message = message.replace('U', 'X')
    return message
