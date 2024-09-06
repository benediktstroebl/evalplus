
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
    message_new = ''
    for letter in message:
        if letter in vowels:
            message_new += letter[2:]
        else:
            message_new += letter
    return message_new

