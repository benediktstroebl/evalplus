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

    # Define the vowels and the character for padding
    vowels = set("aeiouy")
    padding = " "*max(map(len, s.split("")))

    # Check if the last character is 'y'
    if s[-1] == 'y' and s[-2:] == 'yy':
        return s.lower().translate(str.maketrans("", "", vowels)).count('y') + padding.count('y')
    else:
        return s.lower().translate(str.maketrans("", "", vowels)).count('y') + padding.count('y')