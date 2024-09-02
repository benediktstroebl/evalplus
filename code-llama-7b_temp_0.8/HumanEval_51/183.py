

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
    import re
    vowels = ['a','e','i','o','u','y']
    for v in vowels:
        text = text.replace(v, "")
        text = text.replace(v.upper(), "")
    return re.sub(r'[^a-zA-Z]', '', text)
