def vowels_count(s):
    """Returns the number of vowels in the string."""
    c = 0
    for char in s:
        if char in 'aieouAIOU' or (char == 'y' and s.endswith('ay')):
            c += 1
    return c