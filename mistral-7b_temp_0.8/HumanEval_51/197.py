

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
    #you can write your code here.
    #hint: you can use string slicing or list methods to implement this function

    def _remove_vowels(text):
        return "".join([c for c in text if not c in "aeiouAEIOU"])

    return _remove_vowels(text)



