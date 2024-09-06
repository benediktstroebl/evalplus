

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
    # check if the string is empty
    if len(text) == 0:
        return ''
    # check if the string only contains digits
    elif len(text) == 1 and text.isdigit():
        return text
    else:
        vowels = 'aeiouAEIOU'
        result = ''
        for char in text:
            if char not in vowels:
                result += char
        return result
