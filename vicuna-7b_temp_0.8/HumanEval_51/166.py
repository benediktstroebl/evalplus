

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
    vowels = "aeiouAEIOU"
    vowel_count = {}
    for char in text:
        if char.lower() in vowels:
            vowel_count[vowels.index(char.lower())] -= 1
    return ''.join([c for c in text if c.lower() not in vowel_count or vowel_count[vowels.index(c.lower())] > 0])