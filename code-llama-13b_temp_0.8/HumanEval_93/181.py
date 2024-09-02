
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
    for i in message:
        if i.isupper():
            encoded += i.lower()
        else:
            encoded += i.upper()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in vowels:
        if i in encoded:
            x = encoded.find(i)
            encoded = encoded[:x] + encoded[x + 2] + encoded[x + 1] + encoded[x + 3:]
    return encoded
