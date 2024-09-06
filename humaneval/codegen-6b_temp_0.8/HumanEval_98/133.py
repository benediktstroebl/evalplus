
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    n = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            n += 1
    
    return n

assert count_upper('aBCdEf') == 1
assert count_upper('abcdefg') == 0
assert count_upper('dBBE') == 0
assert count_upper('AlAA') == 1
assert count_upper('dBBE') == 1
