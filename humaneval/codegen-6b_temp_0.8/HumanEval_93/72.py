
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
    VOWELS = set(['a','e','i','o','u'])
    result = []
    for c in message:
        if c.isalpha():
            if c.isupper():
                result.append(to_swapcase(c))
            else:
                result.append(c.lower())
        elif c.lower() in VOWELS:
            result.append(to_swapcase(c.lower()))
        else:
            result.append(c)
    return ''.join(result)