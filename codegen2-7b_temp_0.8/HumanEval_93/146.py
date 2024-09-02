
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
    return ''.join([key if (key in string.ascii_lowercase) else 
                                     value for key, value in
                                        {key: (key.lower() if key.isupper() else key.lower()) for 
                                            key in string.ascii_lowercase}.items() 
                                            if key not in 'aeiou'])
    
