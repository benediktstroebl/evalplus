
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    result = sum(1 for i in range(len(s)) if s[i].isupper())
    
    return result

count_upper_two = lambda x: sum(1 for i in range(len(x)) if x[i].isupper())
