
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
    # swap all letters
    message = ''.join(map(lambda x: x.swapcase(), message))
    # replace all vowels with the one 2 places ahead of it
    message = ''.join(map(lambda x: x.replace(x[::2], x[::2]+'A'), message))
    return message
