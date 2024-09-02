
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
    vowels = 'aeiou'
    vowels_dict = {}
    for v in vowels:
        vowels_dict[v] = chr(ord(v) + 2)
    new_message = ''
    for c in message:
        if c in vowels:
            new_message += vowels_dict[c]
        else:
            new_message += c.upper()
    return new_message
