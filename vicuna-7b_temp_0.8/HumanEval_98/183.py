
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    max_i = len(s) // 2
    for i in range(max_i):
        if s[i] == s[i+1] and s[i].upper() == s[i+1].upper():
            return i + 1
    return max_i
