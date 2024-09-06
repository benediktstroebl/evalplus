
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    if len(s) < 2:
        return 0
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i-2] and s[i] == s[i-3] and s[i] == s[i-1] and s[i] == s[i+1] and s[i] == s[i+2]:
            if s[i-2] == s[i-1] and s[i-2] == s[i+1] and s[i+1] == s[i+2]:
                count += 1
    return count
