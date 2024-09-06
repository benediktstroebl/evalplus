
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
    if not isinstance(message, str):
        raise TypeError('message must be a string')

    # assume a-z and A-Z
    # shift 2 places for each vowel,
    # shift 1 place for every other letter
    # lower case all letters
    # return as a string

    for char in message:
        if char.lower() in 'aeiou':
            pass
        else:
            pass
