
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
    vowels = 'aeiouAEIOU'
    cipher = ''
    for i in message:
        if i in vowels:
            if i.isupper():
                i = chr((ord(i) - ord('A') + 2) % 26 + ord('A'))
            else:
                i = chr((ord(i) - ord('a') + 2) % 26 + ord('a'))
        cipher = cipher + i
    return cipher

