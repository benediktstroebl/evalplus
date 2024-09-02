
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
    message = ''.join(sorted(message)) # sort message to ensure consistent case
    message = ''.join([ letter + ''.join(filter(lambda x: x == v, str(x))) for v, letter in enumerate(message)]) # replace vowels with 2 places ahead
    return message