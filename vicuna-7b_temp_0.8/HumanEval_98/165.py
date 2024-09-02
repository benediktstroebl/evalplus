
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s_upper = [i.upper() for i in s]
    num_upper = 0
    for i in range(0, len(s_upper), 2):
        if s_upper[i] == 'E' and s_upper[i+1] == 'E':
            num_upper += 1
    return num_upper
