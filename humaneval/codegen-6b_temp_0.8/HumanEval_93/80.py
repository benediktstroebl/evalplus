
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
    # method 1
    '''
    vowels = {'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}
    for key, val in vowels.items():
        message = message.replace(key, val)
    return message.swapcase()
    '''
    # method 2
    # vowels = {'a': 'n', 'e': 'o', 'i': 'r', 'o': 'l', 'u': 'u'}
    # return ''.join(vowels.get(c, c) for c in message.lower())
    # return ''.join(c.swapcase() if c in vowels else c for c in message.lower())
    # return message.swapcase()
    return ''.join(a.swapcase() if a.lower() in 'aeiou' else a for a in message)

