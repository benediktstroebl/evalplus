

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
    # Create a list of vowel characters
    vowels = 'aeiouAEIOU'
    
    # Iterate through each character in the string
    for char in text:
        # Check if the character is a vowel
        if char in vowels:
            # If it is, replace it with an empty string
            text = text.replace(char, '')
    
    return text