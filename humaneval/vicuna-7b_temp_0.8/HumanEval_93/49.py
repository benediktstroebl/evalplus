
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
    message = message.upper() # convert message to uppercase
    message = ''.join([c.lower() if c.isalpha() else c for c in message]) # convert to lowercase
    message = message.translate(str.maketrans('', '', string.punctuation)) # remove punctuation
    message = ''.join([c if c.isalpha() else '0' for c in message]) # replace vowels with 0
    message = ''.join([''.join(['0', '1'[c.isupper() and d.islower() or c == d] if c in 'aeiouAEIOU' else '0' for c, d in zip(message, '01')]) for message in [message, message[1:]]]) # replace vowels
    return message

