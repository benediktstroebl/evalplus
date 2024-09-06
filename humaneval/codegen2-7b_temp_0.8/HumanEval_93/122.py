
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
    message = message.replace("a", "*")
    message = message.replace("e", "*")
    message = message.replace("i", "*")
    message = message.replace("o", "*")
    message = message.replace("u", "*")
    message = message.replace("y", "*")
    message = message.replace("t", "*")
    message = message.replace("s", "*")
    return
