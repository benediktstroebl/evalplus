
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s = s.upper()
    if s[0] == s[2] == s[4] == s[6] == s[8]:
        return len(s) % 2
    return 0
