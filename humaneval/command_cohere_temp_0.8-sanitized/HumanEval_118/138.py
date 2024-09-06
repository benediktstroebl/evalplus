def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end don't count.
    Empty string if no qualifying vowel is found.
    
    Args:
        word (str): Input word with only English letters.
    
    Returns:
        str: Closest vowel to the right of the word.
    """
    # Ensure input is lowercase for consistency in comparison
    word = word.lower()
    vowel_count = 0

    for char in word:
        if char in 'aeiou':
            vowel_count += 1
            if vowel_count == 2:  # Found two vowels, must be the closest one
                return char
        elif char in 'qwrtzpyfgcmblkhjvn':  # All other characters are consonants
            vowel_count = 0
    return ''