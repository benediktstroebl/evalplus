

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
    # find all vowel characters
    vowels = 'aeiouAEIOU'
    vowel_chars = [c for c in vowels if c in text]
    
    # build list of character indices to be replaced
    indices = [i for i, c in enumerate(text) if c not in vowel_chars]
    
    # replace characters
    return ''.join(indices)
