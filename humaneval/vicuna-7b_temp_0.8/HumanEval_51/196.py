

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
    # change all a's to 'a', all e's to 'e', all i's to 'i', all o's to 'o', and all u's to 'u'
    text = text.translate(str.maketrans('aeiou', 'aeiou'))
    # split the string into a list of characters
    text = text.split()
    # convert the list of characters to a string
    text = ''.join(text)
    return text
