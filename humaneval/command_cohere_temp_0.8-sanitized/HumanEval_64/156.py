def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    """
    vowel = "aeiouy"
    num_vowels = 0
    for char in s:
        if char in vowel:
            num_vowels += 1
    return num_vowels