
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
    for i in range(len(message)):
        if message[i] == 'a' or message[i] == 'e' or message[i] == 'i' or message[i] == 'o' or message[i] == 'u' or message[i] == 'y':
            message = message[:i] + message[i-2:i] + message[i] + message[i+1:]
    return message

