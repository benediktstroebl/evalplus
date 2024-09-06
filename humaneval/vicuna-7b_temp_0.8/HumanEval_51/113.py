

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
    # Create an empty string list to store the characters
    characters = []
    
    # Iterate through the text using a for loop
    for char in text:
        # Check if the character is a vowel
        if char.lower() in "aeiou":
            # If it is, add it to the characters list
            characters.append(char)
        else:
            # If it's not, append it to the characters list
            characters.append(char)
    
    # Remove all the vowels from the characters list
    # and return the result
    return ''.join(characters)
