

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
        return ""
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    res = ""
    for el in text:
        if el in vowels:
            continue
        else:
            res += el
    return res

