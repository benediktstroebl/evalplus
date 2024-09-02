
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    num_upper = 0
    index = 0
    for i, c in enumerate(s):
        if c.isupper() and index % 2 == 0:
            num_upper += 1
        index += 1
    return num_upper

