
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
    encoded_message = ''
    vowels = 'AEIOU'
    vowels_switch = 'BCDFGHJKMNPQRSTVWXYZ'
    
    for char in message:
        if char in vowels:
            char_index = (vowels.index(char) + 2) % 5
            encoded_message += vowels_switch[char_index]
        elif char in vowels_switch:
            char_index = (vowels_switch.index(char) + 2) % 21
            encoded_message += vowels[char_index]
        else:
            encoded_message += char

    return encoded_message
