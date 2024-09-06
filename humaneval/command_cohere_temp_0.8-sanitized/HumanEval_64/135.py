def vowels_count(s):
    """Returns the number of vowels in the string."""
    c = 0
    for char in s:
        if char in 'aieouAIOU':
            if char == 'y' and s.endswith(char):
                c += 1
            else:
                c += 1
        elif char == 'y' and s.endswith(char):
            c += 1
    return c