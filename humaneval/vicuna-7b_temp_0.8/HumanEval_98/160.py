
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    n = len(s)
    count = 0
    i = 0
    while i < n:
        if s[i] == s[i+1] and s[i].isupper():
            count += 1
            i += 1
        elif s[i] != s[i+1]:
            count = 1
            i += 1
    return count
