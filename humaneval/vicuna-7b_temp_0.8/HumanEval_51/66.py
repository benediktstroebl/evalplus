

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
    # create a dictionary of vowels and their ASCII codes
    vowels = "aeiouAEIOU"
    vowel_codes = {c: ord(c) for c in vowels}
    
    # loop through each character in the string
    output = ''
    for char in text:
        # check if the character is a vowel and its ASCII code is in the vowel dictionary
        if char.lower() in vowel_codes and vowel_codes[char.lower()] in vowel_codes:
            # if the character is a vowel, remove it from the string
            output = output.replace(char, '')
    return output
