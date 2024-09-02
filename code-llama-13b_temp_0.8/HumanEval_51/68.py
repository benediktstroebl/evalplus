

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
    text = list(text)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    while len(text) > 0 and text[0] in vowels:
        text.pop(0)
    while len(text) > 0 and text[-1] in vowels:
        text.pop()
    if len(text) == 0:
        return ''
    for i in range(1, len(text)):
        if text[i] in vowels and text[i-1] in vowels:
            text[i] = ''
    return ''.join(text)
