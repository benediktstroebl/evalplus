

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
    # Make an empty string
    new = ""
    # loop through the text
    for x in text:
        # if the char is a vowel
        if x.lower() in "aeiou":
            # dont add it to new string
            continue
        # else add it to new string
        else:
            new += x
    # return the new string
    return new
