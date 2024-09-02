
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
    
    #Encode
    code = ''
    for i in message:
        if i.isalpha():
            code += i
            if i.lower() == 'a':
                code += 'C'
            elif i.lower() == 'e':
                code += 'E'
            elif i.lower() == 'i':
                code += 'H'
            elif i.lower() == 'o':
                code += 'N'
            elif i.lower() == 'u':
                code += 'S'
            else:
                code += chr((ord(i)+2) % 26 + ord('A'))
        else:
            code += i
    return code
