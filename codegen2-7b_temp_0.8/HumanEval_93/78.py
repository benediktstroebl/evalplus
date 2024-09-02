
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
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    message = message.upper()
    
    for i in range(len(message)):
        if message[i] in alphabet:
            if i < len(message) - 1 and message[i] in alphabet and message[i + 1] in alphabet:
                message = message.replace(message[i], message[i + 1])
                message = message.replace(message[i].upper(), message[i + 1].upper())
                
