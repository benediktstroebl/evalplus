
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

    
    
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    message = message.lower()
    
    for index, letter in enumerate(message):
        
        if letter in vowels:
            message = message[0:index] + message[index+2] + message[index+1] + message[index+3:]
    
    for index, letter in enumerate(message):
        if letter in vowels:
            message = message[0:index] + message[index+2] + message[index+1] + message[index+3:]
    
    return message
    
