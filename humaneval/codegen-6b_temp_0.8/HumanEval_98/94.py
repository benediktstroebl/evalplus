
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels_upper = 0
    for i in xrange(len(s)):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90) and (i % 2 == 0):
            vowels_upper += 1
    return vowels_upper
