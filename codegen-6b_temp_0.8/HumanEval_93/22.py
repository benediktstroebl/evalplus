
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
    output = ''
    for letter in message:
        if not letter in 'aeiou':
            output += letter
        elif letter == 'a':
            output += '1'
        elif letter == 'e':
            output += '2'
        elif letter == 'i':
            output += '3'
        elif letter == 'o':
            output += '4'
        elif letter == 'u':
            output += '5'
        else:
            output += letter
    return output