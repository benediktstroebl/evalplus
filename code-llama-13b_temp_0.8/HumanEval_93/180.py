
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
    vowels = 'aeiou'
    vowels_enc = 'bdfhjklmnprstvwz'
    encoded_message = ''
    for char in message:
        if char.lower() in vowels:
            index = (vowels.index(char.lower()) + 2) % 10
            encoded_message += vowels_enc[index]
        elif char.lower() in vowels_enc:
            index = (vowels_enc.index(char.lower()) - 2)
            if index < 0:
                index = 10 + index
            encoded_message += vowels[index]
        else:
            encoded_message += char
    return encoded_message

