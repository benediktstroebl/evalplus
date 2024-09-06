
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
    # You can write your code here!
    msg = ''.join(c.lower() for c in message)
    result = ''
    vowels = 'aeiou'
    for c in msg:
        if c.isalpha():
            if c in vowels:
                result += chr((ord(c) + 2) % 26 + ord('a'))
            else:
                result += chr((ord(c) + 1) % 26 + ord('a'))
        else:
            result += c
    return result

