
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
    
    if not isinstance(message, str):
        raise TypeError('message must be a string')
    
    bellow = 'aeiou'
    
    for i, letter in enumerate(message):
        if letter in bellow:
            message = message[:i] + message[i].upper() + message[i+1:i+1] + message[i].upper() + message[i+1:]
    
    return message

