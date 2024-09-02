
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    n = len(s)
    a = 0
    for i in range(n//2):
        if s[i] == s[n-1-i] and s[i].upper() == s[n-1-i].upper():
            a += 1
    return a