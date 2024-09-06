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

    # Define the vowels that will be counted
    vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])

    # Check if the last character of the string is 'y'
    if s[-1] == 'y' and len(s) > 1:
        # If it is, include it in the count
        return len(s) - s.count(vowels)  # excludes 'y' at the end
    else:
        # Otherwise, exclude 'y' and count the other vowels
        return s.count(vowels)