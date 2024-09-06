
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    m, n = len(s), len(s[1:])
    if n > m:
        return 0
    a, b = 0, 0
    for i in range(m):
        if s[i].isupper():
            a += 1
        elif s[i].isupper():
            b += 1
    if b >= (n // 2) % 2:
        return a + 1
    return 0

s = input().strip()
