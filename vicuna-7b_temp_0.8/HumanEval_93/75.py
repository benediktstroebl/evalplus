
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
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(message)):
        if message[i] == 'a':
            j = i + 2
            while j < len(alphabet) and alphabet[j] == 'a':
                j += 2
            message = message[:i] + alphabet[j] + message[i + 1:]
        elif message[i] == 'e':
            j = i + 1
            while j < len(alphabet) and alphabet[j] == 'e':
                j += 1
            message = message[:i] + alphabet[j] + message[i + 1:]
        else:
            message = message[:i] + alphabet[i] + message[i + 1:]
    return message
