
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
    encoded = ""
    for char in message:
        if char.isalpha():
            # swap case
            if char.isupper():
                encoded += chr(ord(char) - 1)
            else:
                encoded += chr(ord(char) + 1)
        else:
            encoded += char
    encoded = encoded.lower()
    for char in encoded:
        if char.isalpha():
            # replace vowel
            if char.isvowel():
                position = char.ord() - 1
                if position < 'a'.ord() or position > 'z'.ord():
                    encoded += chr(position)
                else:
                    encoded += chr((position - 1) % 26 + 1)
            else:
                encoded += char
    return encoded
