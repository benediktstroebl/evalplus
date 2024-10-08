

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

    if not isinstance(text, str):
        raise TypeError("text must be string")
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = ""
    for ch in text:
        if ch.lower() not in vowels:
            result += ch
    return result

