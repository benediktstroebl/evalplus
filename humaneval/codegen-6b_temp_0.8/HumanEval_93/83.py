
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
    def encode_reverse(m): 
        m = m + ' '
        l = ''
        for i in m:
            if i.isalpha():
                l = i + l
        return l[:-1]
    vowels = ['a', 'e', 'i', 'o', 'u']
    message = message.lower()
    for v in vowels:
        if v in message:
            message = message.replace(v, encode_reverse(v))
    return message
       