
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    return len([x for x in s if s.index(x) % 2 == 0 and x in 'AEIOU'])
    
    # Wrong solution:
    # return sum(s[i].isupper() for i in range(len(s)) if i % 2 == 0)
    
    # Another wrong solution:
    # return sum(1 for x in s if x.isupper() and s.index(x) % 2 == 0)
