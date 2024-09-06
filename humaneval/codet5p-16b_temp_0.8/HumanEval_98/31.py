
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    
    vowels = 'AEIOU'
    res = 0
    for i, c in enumerate(s):
        if c in vowels and i % 2 == 0:
            res += 1
    return res
