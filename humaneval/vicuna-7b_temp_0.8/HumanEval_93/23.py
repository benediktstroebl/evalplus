
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
    encoded_message = ''
    for char in message:
        if char.isalpha():
            # swap case
            if char.isupper():
                encoded_char = chr(ord(char) + 32)
            else:
                encoded_char = chr(ord(char) - 32)
        else:
            encoded_char = chr(ord(char))
        encoded_message += encoded_char
    return encoded_message
