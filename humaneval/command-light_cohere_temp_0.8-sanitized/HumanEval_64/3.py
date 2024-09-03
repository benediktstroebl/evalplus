def vowels_count(s):
    return sum(c.lower() == 'a' for c in s)