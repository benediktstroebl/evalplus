
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
    newMessage = []
    for i in message:
        if i.isalpha():
            newMessage.append(i.upper() if i.islower() else i.lower())
        else:
            newMessage.append(i)
    return ''.join(newMessage)
