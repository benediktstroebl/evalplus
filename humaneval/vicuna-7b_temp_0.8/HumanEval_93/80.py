
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
    message = message.replace("a", "2")
    message = message.replace("b", "2")
    message = message.replace("c", "3")
    message = message.replace("d", "4")
    message = message.replace("e", "5")
    message = message.replace("f", "6")
    message = message.replace("g", "7")
    message = message.replace("h", "8")
    message = message.replace("i", "9")
    message = message.replace("i", "9")
    message = message.replace("o", "0")
    message = message.replace("u", "5")
    message = message.replace("v", "1")
    message = message.replace("w", "4")
    message = message.replace("x", "1")
    message = message.replace("y", "3")
    message = message.replace("z", "6")
    return message
