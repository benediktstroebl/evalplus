
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    if len(s) < 2:
        return 0
    return sum(1 for i in range(len(s)) if i%2==0 and s[i] in 'AEIOU')

