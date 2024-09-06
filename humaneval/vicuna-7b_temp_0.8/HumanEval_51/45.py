

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
    # Create an empty string to store the modified string
    modified = ''
    # Loop through the characters in the input string
    for char in text:
        # If the character is a vowel, add it to the modified string
        if char.lower() in 'aeiou':
            modified += char
        # If the character is not a vowel, add it to the modified string
        else:
            modified += char
    return modified