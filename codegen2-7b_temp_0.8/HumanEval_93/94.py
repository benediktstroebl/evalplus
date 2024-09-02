
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
        for j in range(len(message)):
            if message[i] in ['a','e','i','o','u']:
                if j == 0 or j == len(message) - 1:
                    if message[i] == 'a':
                        message = message[:i] + 't' + message[i+1:]
                    else:
                        message = message[:i] + 't' + message[i+1:]
    return
