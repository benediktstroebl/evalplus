

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
    #return text.replace("a","")
    #return text.replace("e","")
    #return text.replace("i","")
    #return text.replace("o","")
    #return text.replace("u","")
    #return text.replace("y","")
    vowels = ("a","e","i","o","u","y")
    new_text = ""
    for letter in text:
        if letter not in vowels:
            new_text += letter

    return new_text
