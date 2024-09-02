
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
    # swap case
    message = ''.join([chr(ord('A') + i) for i in range(len(message))])
    # replace vowels
    message = message.translate(str.maketrans('', '', string.punctuation))
    message = message.translate(str.maketrans('', '', 'aeiou'))
    return message
