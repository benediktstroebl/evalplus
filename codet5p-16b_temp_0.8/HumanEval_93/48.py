
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

    vowels = ['a','e','i','o','u','A','E','I','O','U']
    c = message.lower()
    encode = c[::-1]
    for i in range(len(encode)):
        if encode[i] in vowels:
            encode = encode[:i] + chr(ord(encode[i])+2) + encode[i+1:]
    return encode
    
    
    
