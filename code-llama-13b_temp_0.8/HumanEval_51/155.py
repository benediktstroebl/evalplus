

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
    # return text.translate(str.maketrans({'a':None, 'e':None, 'i':None, 'o':None, 'u':None, 'A':None, 'E':None, 'I':None, 'O':None, 'U':None}))
    return ''.join(c for c in text if c not in 'aeiouAEIOU')

