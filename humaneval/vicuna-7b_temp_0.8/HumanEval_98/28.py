
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    d = {}
    for i in range(len(s)):
        if s[i].isupper():
            if i % 2 == 0:
                d[i] = d.get(i, 0) + 1
    return max(d.values()) + 1
