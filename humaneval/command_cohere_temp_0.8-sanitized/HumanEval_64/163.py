def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Special case: 'y' is also counted as a vowel at the end of a word.

    Example:
    >>> vowels_count("ramatta")
    6
    >>> vowels_count("SYZYGY")
    4
    """
    if not s:
        return 0
    
    # Using string concatenation to simulate string slicing in old Python versions
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += vowels_count(s[char:])
        if char == 'y' and s.endswith(char):
            count += 1
    return count