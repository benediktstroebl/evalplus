
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    num_upper = 0
    for i in range(0, len(s) - 1, 2):
        if s[i].isupper() and s[i + 1].isupper():
            num_upper += 1
    return num_upper
