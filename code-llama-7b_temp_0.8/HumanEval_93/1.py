
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
    # TODO: Write your encode function here
    new = ""
    for c in message:
        if c.isalpha():
            if c in "aeiou":
                new += chr((ord(c) + 2) % 26 + 97)
            elif c.isupper():
                new += chr(ord(c) + 26) % 26 + 65
            else:
                new += chr(ord(c) + 26) % 26 + 97
        else:
            new += c
    return new


