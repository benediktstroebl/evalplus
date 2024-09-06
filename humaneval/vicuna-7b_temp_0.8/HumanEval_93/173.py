
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
    result = ""
    for char in message:
        if char.isalpha():
            index = ord(char) - 64
            if index >= 0 and index <= 25:
                result += chr(index + 97)
            else:
                result += chr(index + 123)
        else:
            result += char
    return result