
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    upper_vowels = ['A','E','I','O','U']
    count = 0
    
    for i in range(len(s)):
        if s[i].isupper() and i%2==0:
            count += 1
            
    return
