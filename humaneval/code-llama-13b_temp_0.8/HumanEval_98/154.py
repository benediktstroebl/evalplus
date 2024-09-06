
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    return sum(x in 'AEIOU' and y % 2 for x, y in enumerate(s))
    #return len([x for x in enumerate(s) if x[1] in 'AEIOU' and x[0] % 2])
