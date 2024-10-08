
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
    vowel_mapping = {
        'A':'E',
        'E':'I',
        'I':'O',
        'O':'U',
        'U':'A',
    }
    encoded = ''
    for letter in message:
        if letter in vowels:
            encoded += vowel_mapping[letter]
        elif letter.upper() in vowels:
            encoded += vowel_mapping[letter.upper()].lower()
        else:
            encoded += letter
    return encoded
