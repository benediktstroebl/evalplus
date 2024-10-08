
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    
    return sum([1 for i in range(1,len(s)+1) if i%2 and s[i-1] in 'AEIOU'])
