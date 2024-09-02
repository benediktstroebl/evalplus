
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # write your code here
    n = len(s)
    count = 0
    for i in range(n-1):
        if s[i] == s[i+2] and s[i] == s[i+4] and s[i] == s[i+6]:
            count += 1
    return count
