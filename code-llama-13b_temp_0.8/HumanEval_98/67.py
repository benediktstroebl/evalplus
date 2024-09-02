
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    if len(s) == 0:
        return 0
    
    if s[0].isupper():
        if s[0] in 'AEIOU':
            return 1 + count_upper(s[1:])
        else:
            return count_upper(s[1:])
    else:
        return count_upper(s[1:])
    
    return 0
