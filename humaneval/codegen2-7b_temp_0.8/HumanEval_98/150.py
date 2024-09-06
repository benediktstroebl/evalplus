
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    i = 0
    for j in range(len(s)):
        if s[j] in ['A', 'E', 'I', 'O', 'U']:
            i += 1
    return i
