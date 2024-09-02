
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
    
    message = list(message)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    for i, char in enumerate(message):
        if char.lower() in vowels:
            message[i] = alphabet[alphabet.find(char.lower()) + 2]
    return ''.join(message)

