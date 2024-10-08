
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
    for i in range(n):
        if s[i] in 'bcdfghjklmnpqrstvwxyz':
            if s[i] == s[i+1] and s[i] == s[i+2] and s[i] == s[i+3]:
                continue
        if s[i] == s[i+1] and s[i] == s[i+2] and s[i] == s[i+3]:
            count += 1
    return count
