

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
    # Build a list of vowel characters
    vowels = 'aeiouAEIOU'
    
    # Remove vowels from the string
    vowel_indices = [i for i, c in enumerate(text) if c in vowels]
    return ''.join(text[i:i+1] for i in vowel_indices)
