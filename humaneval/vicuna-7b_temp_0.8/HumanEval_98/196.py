
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    if not s:
        return 0
    n = len(s)
    cnt = 0
    for i in range(n // 2):
        if s[i] == s[i + 1].upper():
            cnt += 1
    return cnt