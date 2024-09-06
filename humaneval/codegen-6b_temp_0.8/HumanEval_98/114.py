
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    letters = [x for x in s.lower() if x in 'aeiou']
    return sum(x.isupper() for x in letters[::2])
