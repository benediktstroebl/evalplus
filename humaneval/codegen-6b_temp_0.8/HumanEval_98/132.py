
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    counter = 0
    for c in s:
        if c.isupper() and int(c)%2 == 0:
            counter += 1
    return(counter)
