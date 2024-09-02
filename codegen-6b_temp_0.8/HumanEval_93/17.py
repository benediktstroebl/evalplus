
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
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    for i, c in enumerate(message):
        if c in vowels:
            replacement = chr(ord(c) - 2)
            message = message[:i] + replacement + message[i+1:]
    return message


