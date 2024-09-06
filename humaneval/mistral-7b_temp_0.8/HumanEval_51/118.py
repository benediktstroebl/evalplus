

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
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    vowels_string = ""
    for vowel in vowels:
        vowels_string += vowel
    removed_vowels = ""
    for i in range(len(text)):
        if text[i] not in vowels:
            removed_vowels += text[i]
    return removed_vowels

