def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Specifically, it counts 'a', 'e', 'i', 'o', 'u', and 'y' as vowels,
    but only when 'y' is at the end of the word.

    Parameters:
    s (str): The input string to count vowels in.

    Returns:
    int: The number of vowels in the string.
    """
    count = 0
    for char in s:
        if char in "aieou":
            count += 1
        elif char == 'y' and s.endswith(char):
            count += 1
    return count