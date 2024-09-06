
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
    if len(s) == 2:
        if s[0].isupper() and s[1].isupper():
            return 1
        elif s[0].isupper() or s[1].isupper():
            return 0
    for i in range(1, len(s), 2):
        if s[i].isupper():
            return 1
    return 0

