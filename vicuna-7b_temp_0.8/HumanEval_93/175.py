
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
    def _swapcase(s):
        return ''.join([i.upper() if i.isalpha() else i for i in s])
    def _replacevowels(s):
        s = s.lower()
        return s.translate(str.maketrans('aeiou', 'aeiouy2'))
    return _swapcase(_replacevowels(message))