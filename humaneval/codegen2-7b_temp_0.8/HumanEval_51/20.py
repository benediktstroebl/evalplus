

def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    text = text.lower()
    if len(text) == 0:
        return ''
    vowels = 'aeiou'
    if text[0] in vowels:
        text = text[1:]
    if text[-1] in vowels:
        text = text[:-1]
    return text
