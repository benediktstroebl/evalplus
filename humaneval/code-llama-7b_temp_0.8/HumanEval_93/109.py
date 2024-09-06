
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
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = [i for i in alpha]
    d = {}
    for i in range(len(a)):
        d[a[i]] = a[(i+2)%len(a)]
        d[a[i].upper()] = a[(i+2)%len(a)].upper()

    result = ''
    for i in message:
        if i in d:
            result += d[i]
        else:
            result += i
    return result
