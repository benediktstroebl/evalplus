
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    l = len(s)
    n = 0
    for i in range(l):
        if s[i].isupper() and (i+1) % 2 == 0:
            n += 1
    return n
