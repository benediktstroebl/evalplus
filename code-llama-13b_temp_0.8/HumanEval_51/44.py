

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
    # get rid of '\n'
    text = text.replace('\n', ' ')
    # get rid of multiple spaces
    text = ' '.join(text.split())
    # get rid of vowels
    vowels = 'aeiou'
    return ''.join(x for x in text if x.lower() not in vowels)

