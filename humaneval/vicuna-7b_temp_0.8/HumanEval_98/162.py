
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    n = len(s)
    i = n // 2
    count = 0
    for j in range(i, n+1):
        if s[j] == s[i-1] and s[j] == s[i+1] and s[j] == s[i] and s[j] == s[i-2] == 'a':
            count += 1
            i += 1
    return count
