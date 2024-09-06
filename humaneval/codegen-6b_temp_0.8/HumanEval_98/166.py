
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    upper_vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for c in s[1::2] if c.upper() in upper_vowels)
