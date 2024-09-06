def vowels_count(s):
    """Returns the number of vowels in a string s,
    where vowels are 'a', 'e', 'i', 'o', 'u', and 'y' at the end of a word."""
    count = 0
    for c in s:
        if c in 'aieou':
            count += 1
        elif c == 'y' and s.endswith(c):
            count += 1
    return count