

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
    if type(text) is not str:
        raise TypeError("Input can only be a string")

    vowels = 'aeiou'
    vowels_list = [vowels]

    for vowel in vowels:
        if vowel in text:
            vowels_list.append(vowel)

    for vowel in vowels_list:
        text = text.replace(vowel, '')

    return text

