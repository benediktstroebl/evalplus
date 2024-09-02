

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
    text_list = list(text)
    vowels = 'aeiou'
    vowels_set = set(vowels)
    for i in range(len(text_list)):
        if text_list[i].lower() in vowels_set:
            text_list[i] = ''
    return ''.join(text_list)
