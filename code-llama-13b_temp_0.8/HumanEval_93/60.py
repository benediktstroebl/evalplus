
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
    vowels_dict = {
        'a': 'c',
        'e': 'g',
        'i': 'i',
        'o': 'k',
        'u': 'm',
        'A': 'C',
        'E': 'G',
        'I': 'I',
        'O': 'K',
        'U': 'M',
    }
    encoded_message = ''
    for c in message:
        if c.isalpha():
            if c.isupper():
                encoded_message += vowels_dict[c].upper()
            else:
                encoded_message += vowels_dict[c]
        else:
            encoded_message += c
    return encoded_message
