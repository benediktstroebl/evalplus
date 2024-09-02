

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
    if text == '':
        return ''
    vowels = ['a','e','i','o','u']
    new_string = ''
    for letter in text:
        if letter not in vowels:
            new_string = new_string + letter
    return new_string
