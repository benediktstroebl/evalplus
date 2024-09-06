
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
    # Write code to swap case
    message = message.upper()
    message = message.lower()

    # Write code to replace vowels with 2 places ahead
    message = ''.join([letter + 2 for letter in message])
    return message
