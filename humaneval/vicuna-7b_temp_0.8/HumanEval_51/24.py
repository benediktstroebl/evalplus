

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
    # Replace vowels with empty string
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove all non-alphanumeric characters
    text = text.translate(str.maketrans('', '', string.digits))
    # Split the string into a list of characters
    text = text.split()
    # Remove all characters that are not alphabetic
    text = [x for x in text if x.isalpha()]
    return ''.join(text)