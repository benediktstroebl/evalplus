def vowels_count(s):
    """Returns the number of vowels in the string."""
    vowel = "aeiouy"
    count = 0
    for char in s:
        if char in vowel:
            count += 1
    return count