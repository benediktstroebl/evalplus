def vowels_count(s):
    """Returns the number of vowels in the string."""
    cnt = 0
    for c in s:
        if c in 'aeiouAEIOU':
            cnt += 1
        elif c == 'y' and s[-1] != 'y':
            cnt += 1
    return cnt