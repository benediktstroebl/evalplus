
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    # make list
    s_list = list(s)
    
    # count of uppercase vowels in even indices
    count = 0
    
    # loop through string
    for i in range(0, len(s_list), 2):
        # if uppercase vowel
        if s_list[i] in ('A','E','I','O','U'):
            count += 1
    
    # return count
    return count
    
    
