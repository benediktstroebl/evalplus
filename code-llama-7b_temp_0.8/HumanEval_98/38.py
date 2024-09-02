
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    result = 0
    for i, e in enumerate(s):
        if e.isupper() and (i % 2) == 0:
            result += 1
    return result

