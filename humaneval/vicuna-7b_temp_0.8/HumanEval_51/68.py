

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
    vowels = 'aeiouAEIOU'
    text_lower = text.lower()
    text_length = len(text_lower)
    vowel_count = 0
    for i in range(text_length):
        if text_lower[i] in vowels:
            vowel_count += 1
            if vowel_count > 1:
                break
        else:
            vowel_count = 0
    return text_lower[:vowel_count]
