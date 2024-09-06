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

    # Define the vowels that are to be counted
    vowels = set('aeiouy')

    # Check if y is at the end of the string and if so, add it to vowels
    if s[-1] == 'y' and s[-2:] == 'y':
        vowels.add('y')

    # Count the number of vowels in the string
    count = sum(1 for char in s if char in vowels)
    return count