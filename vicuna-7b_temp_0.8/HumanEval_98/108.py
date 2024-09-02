
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # check if string is empty
    if len(s) == 0:
        return 0
    
    # count number of uppercase vowels
    count = 0
    for i in range(len(s) // 2):
        if s[i] == s[i+1] == unichr('A'):
            count += 1
    
    # return count
    return count
