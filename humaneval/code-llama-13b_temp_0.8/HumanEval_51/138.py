

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

    # return "" if string is empty
    if text == "":
        return ""

    # return the first char if it is not vowel
    if text[0] not in "aeiouAEIOU":
        return text[0] + remove_vowels(text[1:])

    # return next char if it is vowel
    return remove_vowels(text[1:])

