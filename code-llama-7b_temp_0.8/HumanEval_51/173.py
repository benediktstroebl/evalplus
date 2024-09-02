

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

    #
    # writing this solution with a simple for loop
    #
    vowels = 'aeiou'
    result = ""
    for x in text:
        if x not in vowels:
            result += x

    return result

    #
    # writing this solution using list comprehension
    #
    vowels = 'aeiou'
    return ''.join([x for x in text if x not in vowels])

    #
    # writing this solution using list comprehension with itertools
    #
    import itertools as it
    vowels = 'aeiou'
    return ''.join([x for x in it.repeat(text) if x not in vowels])


