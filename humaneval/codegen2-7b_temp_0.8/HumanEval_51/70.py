

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
    letters = [ch for ch in text]
    if len(letters)!= len(text):
        raise ValueError('Input must be a string!')
    for i in range(len(text)):
        if text[i] in ['a', 'e', 'i', 'o', 'u']:
            letters[i] = 'B'
    return ''.join(letters)
