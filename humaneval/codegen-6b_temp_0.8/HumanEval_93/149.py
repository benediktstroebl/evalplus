
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
    vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
    
    encoded = message.swapcase()
    for vowel in vowels:
        i = 0
        for j, c in enumerate(encoded):
            if c == vowel:
                encoded = encoded[:j] + encoded[j+1].upper() + encoded[j+2:]
                i = j
                break
        if i > 0:
            encoded = encoded[:i] + encoded[i+1].upper() + encoded[i+2:]

    return encoded
