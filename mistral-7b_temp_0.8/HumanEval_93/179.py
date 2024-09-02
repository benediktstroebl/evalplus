
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
    s = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                s += c.lower()
            else:
                s += c.upper()
        elif c.isupper():
            s += c
        else:
            s += c
    message = s
    vowels = ["a","e","i","o","u"]
    for i in range(len(message)):
        if message[i].lower() in vowels:
            message = message[:i] + message[i+1:]
            message = message[:i] + chr(ord(message[i].lower())+2) + message[i+1:]
    return message

