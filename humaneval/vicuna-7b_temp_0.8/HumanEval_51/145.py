

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
    # create a set of vowels
    vowels = "aeiouAEIOU"
    
    # loop through the characters in the string
    result = []
    for char in text:
        # check if the character is a vowel
        if char.lower() in vowels:
            result.append(char)
        else:
            # add the current character to the result list
            result.append(char)
    return "".join(result)

