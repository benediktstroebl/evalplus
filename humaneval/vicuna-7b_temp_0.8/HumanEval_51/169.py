

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
    # create a list of vowel characters
    vowels = 'aeiouAEIOU'
    
    # loop through each character in the input string
    for char in text:
        # check if the character is a vowel
        if char in vowels:
            # if it is, remove it from the string
            text = text.replace(char, '')
    return text
