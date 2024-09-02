
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s = ''.upper()
    i = 1
    for c in s:
        if c.isupper():
            if i % 2 == 0:
                count += 1
            i += 1
    return count
