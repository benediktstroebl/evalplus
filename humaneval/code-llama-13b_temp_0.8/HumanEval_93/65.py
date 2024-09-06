
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
    vowels = 'aeiou'
    encoded = []
    for letter in message:
        letter = letter.lower()
        if letter in vowels:
            idx = (vowels.index(letter) + 2) % 5
            letter = vowels[idx]
        encoded.append(letter.upper())
    return ''.join(encoded)
