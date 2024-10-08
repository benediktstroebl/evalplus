
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
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                pos = ord(char) - 13
            else:
                pos = ord(char) - 2
            new_char = chr(pos + 97)
            result += new_char
        else:
            result += char
    return result
