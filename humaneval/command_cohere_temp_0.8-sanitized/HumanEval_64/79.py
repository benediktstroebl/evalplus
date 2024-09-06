def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Specifically, it counts 'a', 'e', 'i', 'o', 'u', and 'y' as vowels,
    but only when 'y' is at the end of the word.

    Parameters:
    s (str): The input word whose vowels are to be counted.

    Returns:
    int: The number of vowels in the input word.
    """
    # Define the vowels and the character 'y' which is to be counted as a vowel
    vowels = set('aeiouy')
    
    # If the set of characters in the input string contains all the vowels, return the count of vowels
    if set(s) >= vowels:
        return len(s) - s.count(set(s) - vowels)
    
    # Otherwise, return 0
    return 0