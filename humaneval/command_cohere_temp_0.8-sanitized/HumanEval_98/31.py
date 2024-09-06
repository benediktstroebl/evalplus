def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    Example:
    >>> count_upper('aBCdEf')
    1
    >>> count_upper('abcdefg')
    0
    >>> count_upper('dBBE')
    0
    """
    vowels = 'AEIOU'
    count = 0
    length = len(s)
    if length % 2 == 0:
        for i in range(length):
            if s[i] in vowels and s[i].isupper() and (i + 1) % 2 == 0:
                count += 1
    return count