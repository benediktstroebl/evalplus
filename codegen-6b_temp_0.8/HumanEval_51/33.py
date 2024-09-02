

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
    vowels = ['a','e','i','o','u']
    text = text.casefold()
    new_text = []
    for i in range(len(text)):
        if text[i] not in vowels:
            new_text.append(text[i])
    new_text = ''.join(new_text)
    return new_text
