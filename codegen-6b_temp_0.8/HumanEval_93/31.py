
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
    #takes in a message and returns the encoded message
    message = message.lower()
    vowels = "aeiou"
    ret = ""

    for i in range(len(message)):
        if message[i] in vowels:
            ret += chr(ord(message[i]) - 1)
            if i + 2 < len(message):
                ret += chr(ord(message[i + 2]) + 1)
        else:
            ret += message[i]
    return ret
