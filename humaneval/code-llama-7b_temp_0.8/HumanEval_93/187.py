
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
    # Base case
    if not message:
        return message
    # Recursive case
    else:
        # If char is a vowel
        if message[0].lower() in ['a', 'e', 'i', 'o', 'u']:
            return encode(message[1:]) + chr(ord(message[0].lower()) + 2)
        # Otherwise if not a vowel
        else:
            return message[0].lower() + encode(message[1:])
