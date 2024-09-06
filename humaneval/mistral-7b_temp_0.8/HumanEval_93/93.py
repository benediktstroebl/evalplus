
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

    code = ""
    for x in message:
        if x.isupper():
            code += x.lower()
        elif x.islower():
            code += x.upper()
        else:
            code += x

    if code == "":
        return ""
    else:
        code = code.replace('a', 'c')
        code = code.replace('A', 'C')
        code = code.replace('e', 'g')
        code = code.replace('E', 'G')
        code = code.replace('i', 'k')
        code = code.replace('I', 'K')
        code = code.replace('o', 'm')
        code = code.replace('O', 'M')
        code = code.replace('u', 'p')
        code = code.replace('U', 'P')
        return code

