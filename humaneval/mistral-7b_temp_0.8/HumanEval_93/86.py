
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
    # Your code goes here
    out = ''
    for i in message:
        if i.isalpha():
            if i.lower() in 'aeiou':
                if i == 'z':
                    i = 'a'
                else:
                    i = chr(ord(i) + 2)
            out += i.upper() if i.isupper() else i.lower()
    return out
