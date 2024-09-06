
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
    code = {
        "a":"c",
        "e":"g",
        "i":"k",
        "o":"q",
        "u":"t",
        "A":"C",
        "E":"G",
        "I":"K",
        "O":"Q",
        "U":"T"
    }
    encoded = []
    for letter in message:
        if letter in code:
            letter = code[letter]
        encoded.append(letter.upper() if letter.islower() else letter.lower())
    return "".join(encoded)
