

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
    # check for errors
    if not isinstance(text, str):
        raise TypeError("text must be str type")
    # check for empty string and return it as it is
    if not text:
        return text
    # convert text to list
    text_list = list(text)
    # define vowels list
    vowels = ['a', 'e', 'i', 'o', 'u']
    # remove vowels from text_list
    for index, char in enumerate(text_list):
        if char.lower() in vowels:
            del text_list[index]
    # join text_list
    text = ''.join(text_list)
    return text

