
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
    res = ""
    for char in message:
        if char.lower() in "aeiou":
            res += chr(ord(char.lower()) + 2)
        elif char.isupper():
            res += char.lower()
        else:
            res += char
    return res

