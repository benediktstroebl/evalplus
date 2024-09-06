

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
    vowels_lower = "aeiou"
    temp_text = text.lower()
    result = ""
    for i in temp_text:
        if i in vowels or i in vowels_lower:
            result += ""
        else:
            result += i
    return result

