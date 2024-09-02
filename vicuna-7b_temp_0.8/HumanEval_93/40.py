
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
    message = message.upper() # converting message to uppercase
    encoded_message = []
    for char in message:
        if char.isalpha(): # if char is a letter
            if char.isupper(): # if char is uppercase
                # swap case of the letter
                encoded_char = chr(ord(char) - 33)
            else:
                # replace the letter with the letter 2 places ahead of it in the alphabet
                encoded_char = chr(ord(char) + 26)
            encoded_message.append(encoded_char)
        else:
            encoded_message.append(char)
    return encoded_message
