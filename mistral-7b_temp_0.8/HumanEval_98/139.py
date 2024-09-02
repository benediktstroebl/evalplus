
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    u = 0
    if s[::2].isupper():
        u = len(s) - 1
    else:
        for c in s[::2]:
            if c.isupper():
                u += 1
    return u
