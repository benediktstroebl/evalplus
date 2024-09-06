
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
    result = ''
    for char in message:
        # swap case
        if char.isupper():
            result += chr(ord(char) - 1)
        else:
            result += char
    # replace vowels
    result = result.replace('a', 'z')
    result = result.replace('e', 'z')
    result = result.replace('i', 'z')
    result = result.replace('o', 'y')
    result = result.replace('u', 'y')
    return result
