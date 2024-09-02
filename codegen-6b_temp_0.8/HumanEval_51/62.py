

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
    # dont do the following
    # return ''.join([char for char in text if char not in 'aeiouAEIOU'])
    new_text = list(text)
    for i in range(len(new_text)):
        if new_text[i].lower() in 'aeiou':
            new_text[i] = ''
    return ''.join(new_text)
    
