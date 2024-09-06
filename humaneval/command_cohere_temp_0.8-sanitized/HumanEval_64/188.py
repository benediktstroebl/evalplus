def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    vowel characters are 'a', 'e', 'i', 'o', 'u', and special case 'y' at the end.

    Args:
        s (str): The input string to count vowels in.

    Returns:
        int: Number of vowels in the string.
    """
    # define the vowels including the special case
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for v in s:
        if v in vowels:
            count += 1
    # special case for y
    if s.endswith('y') and s != 'y':
        count += 1
    return count