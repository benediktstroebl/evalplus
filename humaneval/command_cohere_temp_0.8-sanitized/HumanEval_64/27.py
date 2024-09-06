def vowels_count(s):
    """
    This function counts the number of vowels in a string.
    Vowels are 'a', 'e', 'i', 'o', 'u', and 'y' at the end of a word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    count = 0
    for char in s:
        if char in "aieou" or (char == 'y' and s.endswith(char)):
            count += 1
    return count