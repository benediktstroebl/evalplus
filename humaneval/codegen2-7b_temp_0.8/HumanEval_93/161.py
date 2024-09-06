
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
    message = message.replace('a', 'A')
    message = message.replace('e', '3')
    message = message.replace('i', '1')
    message = message.replace('o', '0')
    message = message.replace('u', 'U')
    
    return
