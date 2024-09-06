
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
    message = message.upper()
    encoded_message = []
    for char in message:
        if char in 'aeiouAEIOU':
            index = ord(char) - 2
            encoded_char = chr(index)
        else:
            encoded_char = char
        encoded_message.append(encoded_char)
    return encoded_message
