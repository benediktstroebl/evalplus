
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
    vowels = 'AEIOUaeiou'
    encoded_msg = ''
    vowels_count = 0
    for c in message:
        if c in vowels:
            vowels_count += 1
        encoded_msg += c.swapcase()
    for i in range(vowels_count):
        encoded_msg += message[i]
    for c in message[vowels_count:]:
        encoded_msg += c
    return encoded_msg
