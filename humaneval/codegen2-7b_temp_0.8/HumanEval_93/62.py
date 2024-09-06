
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
    
    mapping = {
        'a':'1',
        'e':'3',
        'i':'1',
        'o':'0',
        'u':'1'
        }
    
    return''.join([mapping[c] for c in message.lower()])
    
