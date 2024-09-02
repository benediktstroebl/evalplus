
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    return sum([s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U' for i in range(0, len(s), 2)
