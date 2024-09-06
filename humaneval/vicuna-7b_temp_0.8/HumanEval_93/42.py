
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
    # change the case of all letters
    message = ''.join([chr(ord('a') + i) for i in range(len(message))])
    # replace all vowels with the letter 2 places ahead
    message = message.replace('a', 'b')
    message = message.replace('e', 'c')
    message = message.replace('i', 'd')
    message = message.replace('o', 'e')
    message = message.replace('u', 'f')
    return message
