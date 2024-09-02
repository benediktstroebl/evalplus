

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
    result = ""

    for letter in text:
        if letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u" and letter != "A" and letter != "E" and letter != "I" and letter != "O" and letter != "U":
            result += letter

    return result

