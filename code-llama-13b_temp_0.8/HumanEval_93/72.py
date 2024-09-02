
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
    encoded = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in message:
        letter = letter.lower()
        if letter in vowels:
            encoded += vowels[(vowels.index(letter) + 2) % 5]
        else:
            encoded += letter
    return encoded.upper()
