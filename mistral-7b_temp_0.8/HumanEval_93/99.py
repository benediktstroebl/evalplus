
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

    # your code goes here
    s = message
    a = ''
    for x in s:
        if x.isalpha():
            if x.islower():
                a += x.upper()
            else:
                a += x.lower()
        else:
            a += x
    vowels = 'aeiou'
    for i in range(len(a)):
        if a[i] in vowels:
            if a[i] != 'u':
                a = a[:i] + a[i+1:]
            else:
                a = a[:i] + a[i+2:]
    return a

