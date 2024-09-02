

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
    # if text is '', return ''
    if text == '':
        return ''

    # otherwise remove vowels from text and return it
    else:
        # remove vowels from text
        vowels = 'aoueiy'
        no_vowels = ''
        for letter in text:
            if letter.lower() not in vowels:
                no_vowels += letter

        # return text without vowels
        return no_vowels

