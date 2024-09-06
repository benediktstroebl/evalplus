def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    """
    vowel = "aeiouy"
    count = 0
    for char in s:
        if char in vowel:
            count += 1
    return count