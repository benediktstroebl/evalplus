

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
    # import re
    # vowels = 'aeiou'
    # return re.sub(r'[' + vowels + ']', '', text)

    vowels = "aeiou"
    vowels_list = list(vowels)

    for vowel in vowels_list:
        text = text.replace(vowel, "")
    return text

