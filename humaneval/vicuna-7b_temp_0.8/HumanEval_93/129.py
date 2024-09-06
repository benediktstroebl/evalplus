
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
    message = message.lower()
    encoded = []
    for i, c in enumerate(message):
        if c.isalpha():
            index = ord(c) - 2
            if index < ord('a'):
                index += 26
            encoded.append(chr(index))
        else:
            encoded.append(c)
    return ''.join(encoded)
