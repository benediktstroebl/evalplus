

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
    vowels = set('aeiou')
    text = list(text)
    length = len(text)
    if length == 0:
        return ''
    new_text = []
    for i in range(length):
        if text[i] in vowels:
            continue
        new_text.append(text[i])
    return ''.join(new_text)
