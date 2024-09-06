
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
    message = message.upper()
    encode_message = ""
    for i in message:
        if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            encode_message += chr(ord(i) + 2)
        else:
            encode_message += i
    return encode_message

