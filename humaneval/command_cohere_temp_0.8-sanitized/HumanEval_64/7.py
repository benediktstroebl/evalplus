def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Specifically, it counts 'a', 'e', 'i', 'o', 'u', and 'y' as vowels,
    but only when 'y' is at the end of the word.

    Args:
        s (str): The input string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """

    # Define the vowels and the y character
    vowels = set('aeiouy')
    
    # If the last character is y and the second last is not a vowel, 
    # we subtract 1 from the count
    if s[-1] == 'y' and s[-2:] not in vowels:
        return len(s) - 1
    
    # Otherwise, return the normal count
    return sum(1 for char in s if char in vowels)