
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
    result = []
    for index, letter in enumerate(message):
        if letter == 'a':
            result.append(message[index+1].lower())
        elif letter == 'e':
            result.append(message[index+1].lower())
        elif letter == 'i':
            result.append(message[index+1].lower())
        elif letter == 'o':
            result.append(message[index+1].lower())
        else:
            result.append(letter)
    return ''.join(
