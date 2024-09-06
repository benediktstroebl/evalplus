

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
    for index in range(len(text_list)):
        char = text_list[index]
        if char in 'aeiouAEIOU':
            text_list[index] = ''
    result = ''.join(text_list)
    result = result.replace('\n', ' ')
    if len(result) > 0:
        return result
    else:
        return ''
