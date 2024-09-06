
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
    from string import ascii_lowercase
    vowels = {'a':'', 'e':'', 'i':'', 'o':'', 'u':''}
    result = []
    for l in message:
        if l.lower() in vowels:
            result.append(vowels[l.lower()])
        else:
            result.append(l.translate(str.maketrans(vowels, '^^^' + vowels)))
    return ''.join(result)
    