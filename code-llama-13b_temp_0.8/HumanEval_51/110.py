

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
    # replace all lower case vowels with empty string
    text = text.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
    # replace all upper case vowels with empty string
    text = text.replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")
    return text
