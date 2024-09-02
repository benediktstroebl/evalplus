

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
    return text.replace('a','@').replace('e','3').replace('i','1').replace('o','0').replace('u','$').replace('A','@').replace('E','3').replace('I','1').replace('O','0').replace('U','$')
