
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
    code_dict = {
        'a': 'c',
        'e': 'g',
        'i': 'j',
        'o': 'q',
        'u': 'x',
        'A': 'C',
        'E': 'G',
        'I': 'J',
        'O': 'Q',
        'U': 'X'
    }
    encoded = ''
    for letter in message:
        if letter in code_dict:
            encoded += code_dict[letter]
        else:
            encoded += letter
    return encoded.upper()
