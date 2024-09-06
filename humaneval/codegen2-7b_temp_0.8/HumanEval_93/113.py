
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
    for i in range(len(message)):
        if message[i] in vowels:
            if message[i + 1] in vowels:
                message = message[:i + 1] + message[i + 2] + message[i + 1:i + 3] + message[i + 3:]
            else:
                message = message[:i + 1] + message[i + 2] + message[i + 1:]
    return
