
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    i = 0
    res = 0
    
    while i < len(s):
        if s[i].isupper():
            res += 1
        i += 2
    
    return res
