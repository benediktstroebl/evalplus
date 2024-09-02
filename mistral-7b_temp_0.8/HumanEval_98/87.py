
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    if not s or len(s) < 2:
        return 0

    c = 0
    for i in range(1, len(s), 2):
        if s[i].isupper():
            c += 1

    return c

