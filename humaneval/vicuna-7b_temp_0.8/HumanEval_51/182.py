

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
    # check for empty string
    if not text:
        return ''
    
    # check if text is a vowel
    if text.lower() in ['a', 'e', 'i', 'o', 'u']:
        return ''
    
    # check if text has multiple vowels
    vowels = 'aeiouAEIOU'
    if '[' in text:
        text = text.replace('[', '').replace(']', '')
    if '{' in text:
        text = text.replace('{', '').replace('}', '')
    if text:
        vowels_count = 0
        for char in text:
            if char in vowels:
                vowels_count += 1
            else:
                vowels_count = 0
        if vowels_count == 0:
            return text
        else:
            return text[:-vowels_count]
    else:
        return text
