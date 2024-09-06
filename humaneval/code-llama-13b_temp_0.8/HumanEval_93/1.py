
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
    encode_dict = {'a': 'c', 'e': 'g', 'i': 'j', 'o': 'q', 'u': 'x', 'y': 'z'}
    result = ''
    for char in message:
        if char in encode_dict:
            result += encode_dict[char]
        else:
            result += char.upper()
    return result
