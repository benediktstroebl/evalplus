def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    total = 0
    vowels = 'AEIOU'
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            total += 1
    return total