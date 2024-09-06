
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
    for i in range(len(message)):
        if message[i].islower():
            res += message[i].upper()
        elif message[i].isupper():
            res += message[i].lower()
        else:
            res += message[i]
    res2 = ""
    for i in range(len(res)):
        if res[i] in "aeiou":
            res2 += chr((ord(res[i]) + 2 - 97) % 26 + 97)
        else:
            res2 += res[i]
    return res2


