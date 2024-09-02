
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

    message = message.lower()
    code = message
    vowels = 'aeiou'
    for i in range(len(message)):
        if message[i] in vowels:
            new = message[i+2]
        else:
            new = message[i+1]
        code = code.replace(message[i], new)
    return code
    
