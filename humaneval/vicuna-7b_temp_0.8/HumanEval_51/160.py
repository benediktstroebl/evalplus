

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
    # convert text to lowercase
    text = text.lower()

    # create empty list to store non-vowel characters
    non_vowel_chars = []

    # loop through each character in the text
    for char in text:
        # check if character is a vowel
        if char in "aeiouAEIOU":
            # if it is, add it to the non_vowel_chars list
            non_vowel_chars.append(char)
        elif char == ' ':
            # if it is a space, add it to the non_vowel_chars list
            non_vowel_chars.append(' ')

    # remove all characters in the non_vowel_chars list from the text
    return "".join([c for c in text if c not in non_vowel_chars])
