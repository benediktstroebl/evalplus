def vowels_count(s):
    """Returns the number of vowels in the string."""
    vowel = set(['a', 'e', 'i', 'o', 'u', 'y'])
    res = 0
    for c in s:
        if c in vowel:
            res += 1
        elif c == 'y' and s.endswith(c):
            res += 1
    return res