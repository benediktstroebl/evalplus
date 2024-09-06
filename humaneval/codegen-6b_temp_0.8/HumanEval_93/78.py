
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
    first = 'TGST'
    new_msg = ''
    for char in message.upper():
        if char in 'AEIOU':
            # take index of char and add index of first letter
            new_msg += first[(first.index(char) + 2) % 5]
            # shift index of first letter by 2 for every letter, 
            # so it doesn't get stuck in the first letter
        else:
            # add letter to new message
            new_msg += char

    return new_msg
