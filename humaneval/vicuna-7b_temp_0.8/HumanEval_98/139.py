
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    max_idx = len(s)
    vowels = set(s) - set('aeiou')
    return sum(1 for i in range(max_idx) if s[i].isupper() and vowels.count(s[i].upper()))