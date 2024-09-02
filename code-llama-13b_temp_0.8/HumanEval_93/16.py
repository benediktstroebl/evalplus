
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
    vowels = 'aeiouAEIOU'
    encode_map = {}
    for i, v in enumerate(vowels):
        encode_map[v] = vowels[(i+2) % len(vowels)]
    
    message = message.swapcase()
    for i, c in enumerate(message):
        if c in vowels:
            message = message[:i] + encode_map[c] + message[i+1:]
    
    return message
    
