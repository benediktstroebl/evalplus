

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

    vowels = ['a', 'e', 'i', 'o', 'u']

    if not isinstance(text, str):
        return 'Input should be string'

    if text.isspace():
        return ''

    result = ""
    for char in text:
        if char.islower():
            if char not in vowels:
                result += char
        elif char.isupper():
            if char.lower() not in vowels:
                result += char
        else:
            result += char

    return result

