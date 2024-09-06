def vowels_count(s):
    """Returns the number of vowels in the string."""
    count = 0
    for c in s:
        if c in 'aeiou':
            count += 1
        elif c == 'y' and s.endswith(c):
            count += 1
    return count