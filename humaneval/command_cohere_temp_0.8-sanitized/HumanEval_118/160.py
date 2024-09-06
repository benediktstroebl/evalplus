def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end do not count.
    Empty string if no qualifying vowel is found.
    
    Args:
        word (str): Input word with only English letters.
    
    Returns:
        str: Closest vowel to the right of the word or an empty string.
    """
    # Ensure input is case-sensitive and only contains alphabetic characters
    assert isinstance(word, str) and all(char.isalpha() for char in word)
    
    # Use a sentinel value to identify vowels and iterate through the word
    vowels = set('AEIOUaeiou')
    last_vowel = None
    for char in word:
        if char in vowels:
            last_vowel = char
        elif last_vowel is not None:
            return last_vowel
    return ''