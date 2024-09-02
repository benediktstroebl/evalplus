
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
    message = ''.join(sorted(message))
    message = "".join(sorted(list(message)))
    message = ''.join(sorted(list(message)))
    message = "".join(sorted(list(message)))
    message = ''.join(sorted(list(message)))
    for i in range(len(message) - 1):
        if message[i] in "aeiouAEIOU":
            message = message.replace(message[i], chr((ord(message[i]) + 2) % 26) + chr((ord(message[i]) + 2) % 26))
    return message
