
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
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.isalpha()[-1].isalpha() and char.isalpha()[-2].isalpha():
                encoded_char = chr((ord(char) + 1) % 26 + 65)
            else:
                encoded_char = chr(ord(char) + 1)
        else:
            encoded_char = chr(ord(char) + 1)
        encoded_message += encoded_char
    return encoded_message
