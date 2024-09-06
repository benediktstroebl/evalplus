def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    vowel = set(['a', 'e', 'i', 'o', 'u', 'y'])
    if not s:
        return 0
    if s[-1] == 'y' and len(s) > 1:
        return sum(1 for char in s if char in vowel) + 1
    else:
        return sum(1 for char in s if char in vowel)