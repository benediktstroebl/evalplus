
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    #return len( [c for c in s if c.isupper() and (s.index(c) % 2 == 0)] )
    #return sum(1 if c.isupper() and (s.index(c) % 2 == 0) else 0 for c in s)
    count = 0
    for i, c in enumerate(s):
        if c.isupper() and (i % 2 == 0):
            count += 1
    return count

