
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for c in s:
        if c.isupper():
            if s[0]!= 'B' and s[1]!= 'B':
                count += 1
    return
