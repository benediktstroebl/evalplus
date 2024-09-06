
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # count_upper('aBCdEf')
    # s[:] = ['a', 'B', 'C', 'd', 'E', 'f']
    # s[1::2] = ['B', 'd', 'E']
    # s[1::2].count('E')
    return s[1::2].count('E')
    
    # return sum(s[i] in 'AEIOU' for i in range(1, len(s), 2))
