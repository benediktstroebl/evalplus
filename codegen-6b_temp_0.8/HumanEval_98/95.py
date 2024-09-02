
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    N = len(s)
    vowels = 'AEIOU'
    counter = 0
    
    for i in xrange(0, N, 2):
        if s[i].upper() in vowels:
            counter += 1
    
    return counter