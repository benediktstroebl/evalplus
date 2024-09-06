
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
    vowels = "AEIOUaeiou"
    mapping = {}
    for i in vowels:
        mapping[i] = chr(ord(i) + 2)
    mapping[" "] = " "
    return "".join([mapping[i] if i in mapping else i.swapcase() for i in message])
