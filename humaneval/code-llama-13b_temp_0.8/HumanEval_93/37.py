
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
    encoded_message = ''
    for i in message:
        if i.isupper():
            encoded_message += chr(ord(i) - ord('A') + 2)
        elif i.islower():
            encoded_message += chr(ord(i) - ord('a') + 2)
    return encoded_message
    
