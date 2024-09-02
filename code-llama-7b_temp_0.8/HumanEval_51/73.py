

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
    # while 'a' in text:
    #     text = text.replace('a', '')
    # while 'e' in text:
    #     text = text.replace('e', '')
    # while 'i' in text:
    #     text = text.replace('i', '')
    # while 'o' in text:
    #     text = text.replace('o', '')
    # while 'u' in text:
    #     text = text.replace('u', '')
    text = text.replace('a', '')
    text = text.replace('e', '')
    text = text.replace('i', '')
    text = text.replace('o', '')
    text = text.replace('u', '')
    return text

