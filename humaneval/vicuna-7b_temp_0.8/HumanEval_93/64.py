
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
    message = message.upper() # converting message to uppercase
    # swapping the case of all letters
    message = message.swapcase()
    # replacing all vowels with 2 places ahead of that vowel
    message = message.replace('a', 'z')
    message = message.replace('e', 'z')
    message = message.replace('i', 'z')
    message = message.replace('o', 'z')
    message = message.replace('u', 'z')
    return message
