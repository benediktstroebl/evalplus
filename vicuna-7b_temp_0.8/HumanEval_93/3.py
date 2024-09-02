
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
    encoding = []
    for char in message:
        if char.isalpha():
            # if it's a letter, swap it
            encoding.append(chr(ord(char) + 26))
        else:
            encoding.append(char)
    return encoding