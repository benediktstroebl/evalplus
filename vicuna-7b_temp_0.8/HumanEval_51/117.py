

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
    # create a set of vowels
    vowels = 'aeiouAEIOU'
    # remove vowels from the text
    text_lower = text.lower()
    vowel_count = 0
    for char in text_lower:
        if char in vowels:
            vowel_count += 1
        else:
            vowel_count = 0
    if vowel_count > 0:
        return text[:-vowel_count]
    else:
        return text