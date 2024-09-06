
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
    mapping = {
        'a': 'c',
        'e': 'g',
        'i': 'j',
        'o': 'm',
        'u': 'w',
        'y': 'aa',
        'A': 'C',
        'E': 'G',
        'I': 'J',
        'O': 'M',
        'U': 'W',
        'Y': 'AA',
    }

    return ''.join([mapping.get(letter, letter) for letter in message])

