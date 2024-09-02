
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
    # Encode the message
    # Encoding the message
    # Encode the message
    
    # Initialise counter
    counter = 0
    
    # Iterate through the message
    for i in message:
        # Swap case of all letters
        if i.isalpha():
            counter +=1
            temp = i.swapcase()
            message = message.replace(i,temp)
            
    
    # Check if every letter is uppercase, if not, swapcase and remove leading/trailing spaces
    if message.isupper():
        message = message[0].swapcase()+message[1:]
    else:
        message = message.swapcase()
            
    
    # Return the message
    return message
    