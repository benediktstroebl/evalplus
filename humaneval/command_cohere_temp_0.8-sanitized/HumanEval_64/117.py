def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    vowel = set(['a', 'e', 'i', 'o', 'u', 'y'])
    cnt = 0
    for c in s:
        if c in vowel:
            cnt += 1
    return cnt