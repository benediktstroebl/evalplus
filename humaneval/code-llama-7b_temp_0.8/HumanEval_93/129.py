
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
    for char in message:
        if char == 'a':
            encoded += 'D'
        elif char == 'e':
            encoded += 'F'
        elif char == 'i':
            encoded += 'H'
        elif char == 'o':
            encoded += 'J'
        elif char == 'u':
            encoded += 'N'
        elif char.isupper():
            if ord(char) - 64 == ord('Z'):
                encoded += chr(64)
            else:
                encoded += chr(ord(char) + 64)
        else:
            encoded += char
    return encoded
