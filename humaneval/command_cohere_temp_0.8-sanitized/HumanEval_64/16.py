def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Valid vowels are 'a', 'e', 'i', 'o', 'u', and 'y' at the end of a word.

    Args:
        s (str): The input string to count the vowels in.

    Returns:
        int: The number of vowels in the string.
    """

    # Define the vowels that will be counted
    vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])

    # Ensure the y is checked only at word endings
    if s[-1] == 'y' and s[-2] != 'y':
        vowels.add('y')

    # Use a set to efficiently count the vowels
    return len(vowels) if s.lower() == s else 0