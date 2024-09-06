
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
    message = message.upper() # convert to uppercase
    message = message.translate(str.maketrans('', '', string.punctuation)) # remove punctuation
    for i in range(len(message)):
        if message[i] in 'aeiouAEIOU':
            message[i] = chr(ord(message[i]) + 2)
    return message