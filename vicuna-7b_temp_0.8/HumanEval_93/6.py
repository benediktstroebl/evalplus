
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
    encoded_message = ''
    for char in message:
        # swap case
        if char.isalpha():
            if char.isupper():
                encoded_char = chr(ord(char) - 33)
            elif char.islower():
                encoded_char = chr(ord(char) + 33)
            else:
                encoded_char = char
        else:
            encoded_char = char
        # replace vowels
        if char == 'a':
            encoded_char = chr(ord(char) + 26)
        elif char == 'e':
            encoded_char = chr(ord(char) + 23)
        elif char == 'i':
            encoded_char = chr(ord(char) + 20)
        elif char == 'o':
            encoded_char = chr(ord(char) + 18)
        elif char == 'u':
            encoded_char = chr(ord(char) + 15)
        else:
            encoded_char = char
        encoded_message += encoded_char
    return encoded_message
