
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
    message = ''.join(map(lambda x: x.upper() if x.isalpha() else x, message))
    message = ''.join(map(lambda x: x.lower() if x.isalpha() else x, message))
    message = ''.join(map(lambda x: x.upper() if x.isalpha() and x.isupper() else x, message))
    message = ''.join(map(lambda x: x.upper() if x.isalpha() and x.isupper() else x.upper() if x.isupper() else x if x.isalpha() else '' for x in 'aeiouAEIOU'.split('')))
    message = ''.join(map(lambda x: x.upper() if x.isalpha() else x.upper() if x.isupper() else x if x.isalpha() else x.lower() if x.isalpha() else '' for x in message))
    message = message.translate(str.maketrans('', '', ''), '').lower()
    return message