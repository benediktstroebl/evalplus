def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Here, 'y' is also a vowel, but only when it is at the end of the word.
    """
    vowel = "aeiouy"
    cnt = 0
    for c in s:
        if c in vowel:
            cnt += 1
    if s.endswith("y") and s != "ay":
        cnt += 1
    return cnt