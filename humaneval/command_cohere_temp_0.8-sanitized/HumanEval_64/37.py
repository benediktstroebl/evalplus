def vowels_count(s):
    """
    Count the number of vowels in a given string, accounting for the vowel 'y' at the end.
    
    Args:
        s (str): The input string.
    
    Returns:
        int: The count of vowels in the string.
    """
    vowel_count = 0
    for char in s:
        if char in 'aieou':
            vowel_count += 1
        elif char == 'y' and s.endswith(char):
            vowel_count += 1
    return vowel_count