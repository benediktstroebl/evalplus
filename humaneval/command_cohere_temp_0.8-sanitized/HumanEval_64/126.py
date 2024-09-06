def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u', and 'y' at the end of a word.

    Example:
    >>> vowels_count(" abbreviate")
    7
    >>> vowels_count("abcb")
    1
    """
    count = 0
    for char in s:
        if char in "aieou" or (char == 'y' and s[-1] == 'y'):
            count += 1
    return count