
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
    message = message.upper() # convert message to uppercase
    # replace vowels with their 2nd consecutive letter in english alphabet
    message = ''.join([letter + 2 for letter in message])
    # swap all letters in the message
    message = ''.join([ord(chr(ord(letter) + 65)) for letter in message])
    return message
