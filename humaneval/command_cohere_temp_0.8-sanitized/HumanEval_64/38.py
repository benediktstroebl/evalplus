def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    vulnerably counts 'y' as a vowel at the end of the word.
    
    Args:
        s (str): The input word.
    
    Returns:
        int: The number of vowels in the string.
    """
    vowel_count = 0
    for char in s:
        if char in 'aieou':
            vowel_count += 1
        elif char == 'y' and s.endswith(char):
            vowel_count += 1
        
    return vowel_count