
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'
    encoded = ''
    for char in message:
        if char.lower() in vowels:
            index = (alphabet.index(char.lower()) + 2) % 26
            encoded += vowels[index]
        else:
            encoded += char.lower() if char.isupper() else char.upper()
    return encoded
    
