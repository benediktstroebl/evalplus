

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
    if not text:
        return ''
    
    # check if the string contains only vowels
    vowels = 'aeiouAEIOU'
    if ' ' in text and text.split(' ')[0] in vowels:
        return ''
    
    # remove vowels from the string
    return ''.join(filter(lambda x: x.isupper() or x.isdigit() or x == ' ' or x == '_' or x == '`', text))
