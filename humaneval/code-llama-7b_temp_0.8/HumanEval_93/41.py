
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
    # pass
    new_message = ""
    for i in range(len(message)):
        if message[i].isalpha():
            if message[i].isupper():
                new_message += message[i].lower()
            else:
                new_message += message[i].upper()
        elif message[i].lower() in 'aeiou':
            new_message += chr(ord(message[i].lower())+2)
        else:
            new_message += message[i]
    return new_message
    
