def vowels_count(s):
    """
    Counts the number of vowels in a string, with the exception of 'y' as a vowel only at the end.

    Args:
        s (str): Input string.

    Returns:
        int: Number of vowels in the string.
    """
    # Define the vowels without 'y'
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Count the vowels in the string and add one if the last char is 'y'
    return sum(1 for char in s if char in vowels or (s[-1:] == 'y' and len(s) > 1))