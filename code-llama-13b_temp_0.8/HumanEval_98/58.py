
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    c = 0
    for x in range(0, len(s)):
        if x % 2 == 0 and s[x].isupper() and s[x].lower() in 'aeiou':
            c += 1
    return c
