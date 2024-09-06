
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
    vowels = 'AEIOU'
    
    encoded = ''
    for i in range(len(message)):
        if message[i].upper() in vowels:
            encoded += message[i].upper() + message[i].lower()
        else:
            encoded += message[i]
    return encoded
