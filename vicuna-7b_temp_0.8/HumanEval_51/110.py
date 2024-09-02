

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
    vowels = 'aeiouAEIOU'
    vowel_count = {}
    for char in text:
        if char in vowels:
            vowel_count[vowels.index(char)] -= 1
    for key, value in vowel_count.items():
        if value == 0:
            vowel_count.pop(key)
    return ''.join([c for c in vowel_count if c != ''])

