
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    m, n = len(s), len(s) // 2
    count = 0
    for i in range(m):
        for j in range(i+1, n):
            if s[i] == s[j] and s[i].isupper() and s[j].isupper():
                count += 1
    return count
