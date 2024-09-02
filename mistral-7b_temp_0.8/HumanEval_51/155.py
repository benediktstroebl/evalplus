

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
    # Use a list comprehension to generate a list of characters from the string,
    # excluding any that are vowels.
    vowels = 'aeiou'
    characters = [char for char in text if char not in vowels]

    # Join the list of characters into a string and return it.
    return ''.join(characters)

