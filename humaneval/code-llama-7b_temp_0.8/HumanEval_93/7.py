
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
    # add your code here
    l = ['a','e','i','o','u']
    a = list(message)
    for i in range(len(a)):
        if a[i].lower() in l:
            a[i] = a[i].lower()
            k = l.index(a[i])
            a[i] = a[i].upper()
            a[i] = l[(k+2)%5]
    return "".join(a)



