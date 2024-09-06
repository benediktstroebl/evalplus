
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    n = len(s) // 2
    count = 0
    for i in range(n, len(s)):
        if s[i] == s[i-n]:
            continue
        if s[i].isupper():
            count += 1
    return count
