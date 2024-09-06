def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end do not count.
    Empty string if no qualifying vowel is found.
    
    Args:
        word (str): Input word with only English letters.
    
    Returns:
        str: Closest vowel to the right of the word or an empty string.
    """
    # Ensure input is case-sensitive and only contains letters
    assert isinstance(word, str) and all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in word)
    
    # Define valid vowels to check
    vowels = 'AEIOUaeiou'
    
    # Initialize empty variables to store closest vowel and index
    closest_vowel = ''
    closest_vowel_index = 0
    
    # Iterate through the word char by char
    for i, char in enumerate(word):
        # Ensure consonants are on the right-hand side of the char
        if char not in vowels and (i == 0 or word[i-1] in vowels):
            # Update if a closer vowel is found
            if char in vowels and (closest_vowel_index == 0 or i < closest_vowel_index):
                closest_vowel = char
                closest_vowel_index = i
    
    # Return the closest vowel if found, otherwise an empty string
    return closest_vowel or ''