
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
    vowels_lower = 'aeiou'
    vowels_upper = 'AEIOU'
    message = list(message)
    for i, letter in enumerate(message):
        if letter in vowels:
            if letter in vowels_lower:
                message[i] = vowels_lower[vowels_lower.index(letter)+2]
            elif letter in vowels_upper:
                message[i] = vowels_upper[vowels_upper.index(letter)+2]
        message[i] = message[i].swapcase()
    return ''.join(message)
