
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
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.isvowel():
                encoded_char = chr((ord(char) + 2) % 26)
            else:
                encoded_char = chr(ord(char))
            encoded_message += encoded_char
        else:
            encoded_message += chr(ord(char))
    return encoded_message
