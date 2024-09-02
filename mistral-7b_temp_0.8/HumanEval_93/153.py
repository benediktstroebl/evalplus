
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
    def _code(msg, i, code, acc):
        if i == len(msg):
            return acc
        else:
            if msg[i] in vowels:
                code = ord(msg[i]) + 2
            else:
                code = ord(msg[i])
            return _code(msg, i + 1, code, acc + chr(code))
    return _code(message, 0, 0, '')

