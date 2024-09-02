

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
    # the following statement is for the HackerRank tests.
    # you can ignore it!
    if text.find('\n') == -1:
        text = text + '\n'
    if text[-1] != '\n':
        text = text + '\n'

    # the following statements are for the doctest tests
    # you can also ignore them
    assert remove_vowels('') == ''
    assert remove_vowels('abcdef\nghijklm') == 'bcdf\nghjklm'
    assert remove_vowels('abcdef') == 'bcdf'
    assert remove_vowels('aaaaa') == ''
    assert remove_vowels('aaBAA') == 'B'
    assert remove_vowels('zbcd') == 'zbcd'

    new_text = ''
    for line in text.split('\n'):
        for letter in line:
            if letter.lower() not in 'aeiou':
                new_text += letter
        new_text += '\n'
    new_text = new_text[:-1]
    return new_text

