
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

    message = message.lower()
    new_message = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in message:
        if c in vowels:
            new_message += vowels[(vowels.index(c) + 2) % 5]
        else:
            new_message += c
    return new_message

