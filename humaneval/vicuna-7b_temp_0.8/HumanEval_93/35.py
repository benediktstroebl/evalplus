
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
            i = ord(char) - 2
            if i < 0:
                i = 25 + i
            if i == 25:
                i -= 2
            if i == 25:
                i -= 2
            result += chr(i)
        else:
            result += char
    return result
