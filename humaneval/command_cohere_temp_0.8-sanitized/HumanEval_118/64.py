def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end do not count.
    Empty string if no qualifying vowel is found.
    
    Args:
        word (str): Input word
    
    Returns:
        str: Closest vowel or empty string if none met the criteria.
    """
    # Ensure input is case-sensitive and lower-cased
    word = word.lower()
    
    # Ensure we don't count vowels at word start OR end
    qualified_positions = word[1:-1].finditer('([aeiou])')
    candidate = next((x.group(1) for x in qualified_positions if x.group(1) not in word), '')
    
    return candidate