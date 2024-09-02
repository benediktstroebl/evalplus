
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
    new_message = []
    for i in message:
        if i in "aeiou":
            new_message.append("X")
        elif i == " ":
            new_message.append(i)
        else:
            new_message.append(chr((ord(i)-32)+2))
    return "".join(new_message)
    
        
        
        
        
        
        
        
        
        
