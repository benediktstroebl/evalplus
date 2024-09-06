

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
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels_str = ''.join(vowels)
    for i in range(len(text)):
        for j in vowels:
            if text[i] == j:
                text = text[:i] + text[i+1:]
                break

    return text

