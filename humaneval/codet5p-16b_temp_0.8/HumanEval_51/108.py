

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

    vowels = "aeiou"
    vowels_list = list(vowels)
    text_list = list(text)
    for i in range(len(text_list)):
        if text_list[i] in vowels_list:
            text_list[i] = ''
    text_without_vowels = ''.join(text_list)
    return text_without_vowels


