

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
    # using if-else statement to check if each letter is a vowel
    # and return the remaining string
    # you can use regular expression to check if the letter is vowel
    # or use set() and check if the set contains vowel
    return ''.join([c for c in text if c not in 'aeiouAEIOU' ])
