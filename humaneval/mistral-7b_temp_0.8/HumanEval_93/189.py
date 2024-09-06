
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
    x = ""
    for i in message:
        if i.islower():
            x += i.upper()
        elif i.isupper():
            x += i.lower()
        elif i in "aeiou":
            x += chr(ord(i) + 2)
        else:
            x += i
    return x
