
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
    # swap case
    message = message.upper() + message.lower()
    
    # replace vowels
    vowels = set('aeiouAEIOU')
    message = ''.join([c if c in vowels else 'S' for c in message])
    
    return message
