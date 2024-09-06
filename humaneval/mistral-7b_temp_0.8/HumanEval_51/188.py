

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
    if text == "":
        return text
    if text[0] == " ":
        return remove_vowels(text[1:])
    else:
        vowels = "aeiouAEIOU"
        if text[0] in vowels:
            return remove_vowels(text[1:])
        else:
            return text[0] + remove_vowels(text[1:])
