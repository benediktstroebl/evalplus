

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
    # <YOUR CODE GOES HERE>
    vowels = 'aeiouAEIOU'
    txt = list(text)
    for i in range(0, len(txt)):
        if txt[i] in vowels:
            txt[i] = ''
    output = ''.join(txt)
    return output
