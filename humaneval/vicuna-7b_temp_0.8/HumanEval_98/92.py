
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    i = 0
    n = len(s)
    while i < n//2:
        if s[i] == s[i+1] == 'B':
            continue
        if s[i] == 'b':
            return 0
        i += 1
    return 1
