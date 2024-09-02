
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            count += 1
    return count
    
    # another solution:
    # return sum(c.isupper() for i, c in enumerate(s) if i % 2 == 0)
