
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
    message = message.upper()
    message = ''.join(sorted(message))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoding = []
    for char in message:
        index = alphabet.index(char)
        if index % 2 == 0:
            index += 1
        else:
            index -= 1
        encoding.append(alphabet[index])
    return ''.join(encoding)
