
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    dp = 0
    for i in range(len(s) // 2):
        if s[i] == s[i+1].upper() and s[i] == 'A' or s[i] == 'a':
            dp += 1
    return dp
