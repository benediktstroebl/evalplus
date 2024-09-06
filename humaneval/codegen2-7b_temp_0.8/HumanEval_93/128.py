
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
    message_copy = message.replace(' ', '')
    message_upper_copy = message_copy.upper()
    vowels = 'AEIOU'
    for index, letter in enumerate(message_upper_copy):
        if letter in vowels:
            message_upper_copy = message_upper_copy.replace(letter, str(index + 2))
    message_upper_copy = message_upper_copy.replace('0', 'S')
    return message_upper_
