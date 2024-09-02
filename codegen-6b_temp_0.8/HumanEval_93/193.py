
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
    vowels = 'aeiou'
    new_str = ''
    for i in message:
        if i.isalpha():
            if i.lower() in vowels:
                new_str += message[message.index(i) + 2].upper()
            else:
                new_str += message[message.index(i) + 2]
        else:
            new_str += i
    return new_str

