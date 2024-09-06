

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
    # convert text to lowercase
    text = text.lower()
    #remove vowels
    vowels = set('aeiou')
    new_text = ''
    for letter in text:
        if letter.lower() not in vowels:
            new_text += letter
    return new_text
