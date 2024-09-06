

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
    # Create a set of vowels and map of vowel characters
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_map = {ord(c): i for i, c in enumerate(vowels)}
    
    # Create a list of strings, where each string is a contiguous sequence of characters
    strings = [c for c in text if c not in vowel_map]
    
    # Return the list of strings as a single string
    return ''.join(strings)