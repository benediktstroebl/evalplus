
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
        if char.isupper():
            before_index = 2 * (ord(char) - ord("A"))
            after_index = 2 * (ord(char) - ord("A") + 25)
            encoded += chr(ord(char) - before_index)
            encoded += chr(ord(char) - after_index)
        else:
            encoded += char
    return encoded
