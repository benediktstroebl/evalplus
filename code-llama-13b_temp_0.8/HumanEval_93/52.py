
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
    encoded_message = ""
    vowels = 'aeiou'
    for c in message:
        if c.isupper():
            new_char = chr(ord(c) + 2)
            if new_char > 'Z':
                new_char = chr(ord(c) - 24)
            encoded_message += new_char.upper()
        elif c.islower():
            new_char = chr(ord(c) + 2)
            if new_char > 'z':
                new_char = chr(ord(c) - 24)
            encoded_message += new_char.lower()
        else:
            encoded_message += c

    return encoded_message
