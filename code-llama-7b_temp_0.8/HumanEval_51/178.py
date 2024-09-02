

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
    if not text:
        return ''
    if text.islower():
        return ''.join(l for l in text if l not in vowels)
    elif text.isupper():
        return ''.join(l.upper() for l in text if l not in vowels)
    else:
        return ''.join(l if l not in vowels else (l.upper() if l.lower() not in text else l) for l in text)

