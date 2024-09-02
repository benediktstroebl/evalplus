

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

    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    new_text = ''
    for c in text:
        if c.lower() not in vowels:
            new_text += c
    return new_text

