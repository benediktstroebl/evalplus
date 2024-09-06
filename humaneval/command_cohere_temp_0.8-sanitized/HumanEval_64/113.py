def vowels_count(s):
    """Returns the number of vowels in the string."""
    cnt = 0
    for c in s:
        if c in 'aeiou':
            cnt += 1
        elif c == 'y' and s.endswith(c):
            cnt += 1
    return cnt