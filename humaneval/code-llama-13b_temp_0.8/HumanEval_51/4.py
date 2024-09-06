

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
    # create a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    new_str = []
    for c in text:
        # check if it is vowel
        if c not in vowels and c.lower() not in vowels:
            # if it is not vowel then add to list
            new_str.append(c)

    return ''.join(new_str)

