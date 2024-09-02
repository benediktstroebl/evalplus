
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    return s.count('A', s.find('A', 0, 1), len(s), 2) + s.count('E', s.find('E', 0, 1), len(s), 2)
