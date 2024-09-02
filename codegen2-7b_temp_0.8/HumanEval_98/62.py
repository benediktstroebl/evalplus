
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    return sum([1 if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U' else 0 for c in s])




