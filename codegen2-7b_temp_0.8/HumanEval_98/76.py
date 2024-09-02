
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    res = 0
    for c in s:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'y':
            res += 1
            
    return
