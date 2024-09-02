
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded = ''
    for char in message:
        if char in vowels:
            char_index = vowels.index(char)
            if char_index < 4:
                new_char = vowels[char_index + 2]
            else:
                new_char = vowels[0]
            encoded += new_char
        else:
            encoded += char.upper()
    return encoded
