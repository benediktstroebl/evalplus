
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
            # replace vowels with 2 places ahead in alphabet
            new_char = "".join([chr(ord("a")+i), chr(ord(char)+i) for i in range(ord(char),ord("a")+1)])
            # swap case of all letters
            new_char = new_char.upper()
            encoded_message += new_char
        else:
            encoded_message += char
    return encoded_message
