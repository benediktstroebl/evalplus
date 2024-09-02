
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    
    
    return sum([s[2*i].lower() in 'aeiou' and s[2*i+1].lower() in 'aeiou' for i in range(len(s)//2)])
    
    
