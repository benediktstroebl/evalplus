
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
    res = ''
    for l in message:
        if l.isalpha():
            if l.lower() in vowels:
                i = vowels.index(l.lower())
                res += vowels[(i+2)%len(vowels)]
            else:
                res += l
        else:
            res += l
    return res
