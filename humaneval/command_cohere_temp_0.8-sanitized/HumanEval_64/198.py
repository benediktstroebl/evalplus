def vowels_count(s):
    """Returns the number of vowels in the string."""
    vowel = set('aeiouy')
    res = 0
    for c in s:
        if c in vowel:
            res += 1
    if s.endswith('y') and not s.endswith('ay') and not s.endswith('by') and not s.endswith('dy'):
        res += 1
    return res