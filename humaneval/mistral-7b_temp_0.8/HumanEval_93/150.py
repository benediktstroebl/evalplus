
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
    vowel_dict = {
        'A':'C',
        'E':'G',
        'I':'K',
        'O':'Q',
        'U':'W'
    }
    for c in vowel_dict:
        message = message.replace(c,vowel_dict[c])
    return message.replace(' ', '')
