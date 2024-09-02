
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
    result = ''
    for char in message:
        if char.isalpha():
            position = ord(char) - 2
            if position < 0:
                position = 0
            if position > 25:
                position = 26
            result += chr(position)
        else:
            result += char
    return result
