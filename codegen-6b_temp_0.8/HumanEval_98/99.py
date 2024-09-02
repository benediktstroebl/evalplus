
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    for i, c in zip(range(len(s), 0, -2), reversed(s)):
        if c.upper() in 'AEIOU':
            if i % 2 == 0:
                yield 1

