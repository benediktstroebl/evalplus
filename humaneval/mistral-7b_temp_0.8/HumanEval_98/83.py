
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    n = 0
    for i in s:
        if i.isupper():
            if(s.index(i)%2 == 0):
                n+=1
    return n
