
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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_message = ''
    for i in message:
        if i.lower() in alphabet:
            new_message += alphabet[(alphabet.index(i.lower()) + 2) % 26]
        else:
            new_message += i
    return new_message
        
