
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
    encoded = ''
    for char in message:
        if char.isalpha():
            # swap case
            char = chr(ord(char) ^ ord('a') + 25)
            # replace vowels
            char = chr(ord(char) ^ ord(char[1]) + 2)
        encoded += char
    return encoded
