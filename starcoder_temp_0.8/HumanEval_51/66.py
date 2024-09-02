

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
    vowels = ["a","e","i","o","u"]
    list_of_str = list(text)
    for i in list_of_str:
        if i.lower() in vowels:
            list_of_str.remove(i)
    return "".join(list_of_str)
