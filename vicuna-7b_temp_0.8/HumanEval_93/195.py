
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
    # convert to lowercase
    message = message.lower()
    
    # swap case of all letters
    message = message.swapcase()
    
    # replace vowels with their uppercase counterparts
    message = message.replace('a', 'A')
    message = message.replace('e', 'E')
    message = message.replace('i', 'I')
    message = message.replace('o', 'O')
    message = message.replace('u', 'U')
    
    # convert to uppercase
    message = message.upper()
    
    return message
