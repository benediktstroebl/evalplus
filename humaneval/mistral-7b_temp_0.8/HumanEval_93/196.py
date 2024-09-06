
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
    for char in message:
        if char.islower():
            char = char.upper()
        elif char.isupper():
            char = char.lower()
        else:
            continue
        vowels = 'aeiou'
        if char in vowels:
            index = vowels.index(char)
            char = vowels[index+2]

        encoded_message += char

    return encoded_message
