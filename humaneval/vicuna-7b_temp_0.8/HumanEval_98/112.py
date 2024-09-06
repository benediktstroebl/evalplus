
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s_upper = ''.upper()
    n = 0
    for i in range(len(s_upper)-1):
        if s_upper[i] == s_upper[i+1] and s_upper[i].isupper():
            n += 1
    return n
