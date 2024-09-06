
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    num_upper = 0
    for i in range(len(s)):
        if s[i] == s[i+1] and s[i].isupper():
            num_upper += 1
    return num_upper