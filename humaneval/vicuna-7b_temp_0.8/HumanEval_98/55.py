
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    N = len(s)
    n = 0
    for i in range(N // 2):
        if s[i] == s[i+1].upper() and s[i] == s[i+2].upper():
            n += 1
    return n
