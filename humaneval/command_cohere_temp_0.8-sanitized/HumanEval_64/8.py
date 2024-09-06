def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    vowel = "aeiouy"
    num_vowels = 0
    for char in s:
        if char in vowel:
            num_vowels += 1
    if s.endswith("y") and s != "y":
        num_vowels += 1
    return num_vowels