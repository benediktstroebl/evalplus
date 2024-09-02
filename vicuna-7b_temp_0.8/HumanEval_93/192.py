
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
    message = message.upper()
    message = message.replace('a', 'z')
    message = message.replace('e', 'z')
    message = message.replace('i', 'x')
    message = message.replace('o', 'y')
    message = message.replace('u', 'z')
    message = ''.join(map(lambda x: 'z' if x == 'y' else x for x in message))
    return message
