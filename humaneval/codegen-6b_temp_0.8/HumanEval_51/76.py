

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
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    new_text = ""
    for i in text:
        if i in vowels:
            new_text += i
    return new_text


