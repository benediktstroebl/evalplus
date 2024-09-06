
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

    import re
    vowels = 'aeiou'
    encoded = ''
    for char in message:
        if char.isupper():
            encoded += char
        else:
            for i in range(len(vowels)):
                if vowels[i] == char.lower():
                    encoded += vowels[(i+2)%len(vowels)].upper()
        
    return encoded
        
