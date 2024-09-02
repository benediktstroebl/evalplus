

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
    # write your answer between #start and #end
    #start
    vowels = ["a", "o", "e", "i", "u"]

    new_text = ''

    for char in text:
        if char in vowels:
            new_text += ''
        else:
            new_text += char

    return new_text
    #end
