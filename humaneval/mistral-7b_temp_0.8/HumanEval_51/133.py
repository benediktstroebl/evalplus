

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
    # the vowels:
    vowels = ['a', 'e', 'i', 'o', 'u']
    # empty string to be returned:
    result = ''
    # loop over string:
    for letter in text:
        # if the letter is not in vowels:
        if letter not in vowels:
            # add it to the result string:
            result += letter
    # return result:
    return result

