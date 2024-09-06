

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
    # convert string to lowercase and split on spaces
    text = text.lower()
    text = text.split()
    
    # remove vowels from each word
    vowels = "aeiouAEIOU"
    words = []
    for char in text:
        if char.lower() not in vowels:
            words.append(char)
    return " ".join(words)
