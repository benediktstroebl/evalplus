

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
    # Assert that the text is a string
    if not isinstance(text, str):
        raise TypeError("text is not a string")

    # Convert text to lowercase
    text = text.lower()

    # Return string without vowels
    return text.translate(str.maketrans('', '', 'aeiou'))
