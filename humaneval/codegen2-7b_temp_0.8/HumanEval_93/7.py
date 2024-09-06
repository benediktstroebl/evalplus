
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
    message = message.replace('a','@').replace('e','3').replace('i','1').replace('o','0').replace('u','$')
    for i in range(len(message)-1):
        if message[i] in 'aeiou':
            message = message[:i] + message[i].upper() + message[i+1:]
    return message
