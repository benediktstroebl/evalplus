
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
    for letter in message:
        if letter.isalpha():
            if letter.lower() in 'aeiou':
                result.append(next(letter for letter in 'bcfgklmnpqrstuvwxyz' if letter.lower() != letter))
            else:
                result.append(next(letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if letter.lower() != letter))
        else:
            result.append(letter)
    return ''.join(result)

