
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
    message = "".join(sorted(message))
    for i in range(len(message)-1):
        if message[i] == "a":
            j = i+2
        elif message[i] == "e":
            j = i+1
        else:
            j = i+1
        message = message[:i] + message[j] + message[i+1:j+2] + message[i+2:]
    return message.upper()
