
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
    to_replace = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 'u': '6', 'y': 'r'}

    for k, v in to_replace.iteritems():
        message = message.replace(k, v)
    
    return message
