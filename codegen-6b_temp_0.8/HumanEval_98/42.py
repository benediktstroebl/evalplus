
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    return sum(s[i].isupper() for i in range(0,len(s),2))

assert count_upper('aBCdEf') == 1
assert count_upper('abcdefg') == 0
assert count_upper('dBBE') == 0

