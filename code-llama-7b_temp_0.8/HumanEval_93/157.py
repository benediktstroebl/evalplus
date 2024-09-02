
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
    
    # replace with your code here
    # a = list(message)
    # for i in a:
    #     if i in 'aeiouAEIOU':
    #         if i in 'aeiou':
    #             a[a.index(i)] = chr(ord(i) + 2)
    #         else:
    #             a[a.index(i)] = chr(ord(i) - 2)
    # return ''.join(a)
    return ''.join(chr(((ord(c) + 1) % 26) + 97) if c.isalpha() else c for c in message)
