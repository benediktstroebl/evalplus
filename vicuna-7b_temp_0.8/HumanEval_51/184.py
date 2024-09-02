

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
    # Create a set of vowel characters
    vowels = set(string.ascii_letters)[:4]
    vowel_count = 0
    
    # Iterate through the text
    for char in text:
        # If the character is a vowel
        if char in vowels:
            # If the character count is less than 4
            if vowel_count < 4:
                # Remove the vowel and decrease the count
                vowel_count -= 1
            else:
                # Remove all vowels at once
                break
        else:
            vowel_count += 1
    
    return ''.join(c for c in text if c not in vowels)
