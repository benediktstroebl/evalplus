

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
    # initialize the vowels list
    vowels = "aeiouAEIOU"
    
    # create a new string without vowels
    new_string = ''
    
    # iterate through each character in the original string
    for char in text:
        # check if the current character is a vowel
        if char in vowels:
            # if the current character is a vowel, add a non-vowel to the new string
            new_string += chr(ord(char) + 1)
        else:
            # if the current character is not a vowel, add it to the new string
            new_string += char
    
    return new_string