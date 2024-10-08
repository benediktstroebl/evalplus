
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

    vowels = ['a','e','i','o','u']
    message = message.lower()
    
    for i in range(len(message)):
        if message[i] in vowels:
            newChar = message[i+2]
        else:
            newChar = message[i+1]
        message = message[:i] + newChar + message[i+1:]
    return message
