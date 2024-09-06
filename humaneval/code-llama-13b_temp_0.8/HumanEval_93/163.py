
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
    shift_key = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 's',
        'u': 'v',
        'A': 'C',
        'E': 'G',
        'I': 'K',
        'O': 'S',
        'U': 'V'
    }
    shifted_message = ''
    for char in message:
        if char in vowels:
            shifted_message += shift_key[char]
        elif char.lower() in vowels:
            shifted_message += shift_key[char.lower()].upper()
        else:
            shifted_message += char
    return shifted_message
