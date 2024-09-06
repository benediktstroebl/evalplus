
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    n = len(s)
    if n % 2 == 0:
        c = 0
        for i in range(n):
            if s[i].isupper():
                c += 1
        return c
    else:
        return 0

s = "abcdefg"
