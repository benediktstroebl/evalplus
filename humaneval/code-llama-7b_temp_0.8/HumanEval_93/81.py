
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
    encode_string = ''
    for character in message:
        if character == 'a':
            encode_string += 'C'
        elif character == 'e':
            encode_string += 'I'
        elif character == 'i':
            encode_string += 'O'
        elif character == 'o':
            encode_string += 'T'
        elif character == 't':
            encode_string += 'A'
        elif character.isupper():
            encode_string += character.swapcase()
        elif character.islower():
            encode_string += character.swapcase()
    return encode_string

