
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
    for i in range(n // 2):
        if s[i] == s[i+1].upper() and s[i] == s[i+2].upper():
            count += 1
    return count
