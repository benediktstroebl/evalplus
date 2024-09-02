

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

    # vowels = 'aeiou'
    # for letter in text:
    #     if letter.lower() in vowels:
    #         text = text.replace(letter, '')
    # return text


    vowels = 'aeiou'
    return ''.join(letter for letter in text if letter.lower() not in vowels)

