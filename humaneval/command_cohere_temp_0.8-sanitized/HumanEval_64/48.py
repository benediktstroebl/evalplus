def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Special case: 'y' is treated as a vowel only at the end of a word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.
    """
    
    # Define vowels and the conditional 'y'
    vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])
    
    # Check for vowels and count them if they are present
    count = sum(1 for char in s if char in vowels)
    
    # Special case: Count 'y' if it is at the end of the word
    if s.endswith('y') and len(s) > 1:
        count += 1
    
    return count