def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Self-defined vowels included.
    """
    vowel = ["a", "e", "i", "o", "u", "y"]
    res = 0
    for char in s:
        if char in vowel:
            res += 1
    return res