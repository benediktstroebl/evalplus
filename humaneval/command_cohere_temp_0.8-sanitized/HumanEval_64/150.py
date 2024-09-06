def vowels_count(s):
    """
    This function counts the number of vowels in a string,
    with the exception of 'y' as a vowel only at the end of a word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    if not s:
        return 0
    count = 0
    for char in s:
        if char in "aieou":
            count += 1
        elif char == 'y' and s.endswith(char):
            count += 1
    return count