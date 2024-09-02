
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    n = len(s)
    result = 0
    for i in range(0, n, 2):
        if s[i] in 'AEIOU':
            result += s[i].isupper()
    return result
