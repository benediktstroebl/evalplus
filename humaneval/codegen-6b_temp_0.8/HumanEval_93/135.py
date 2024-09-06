
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
    vowels = "aeiou"
    for i in range(len(message)):
        if message[i].lower() in vowels:
            idx = vowels.find(message[i].lower())
            encoded += vowels[idx+2].upper()
        else:
            encoded += message[i]
    return encoded
