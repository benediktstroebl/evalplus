
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    i = 0
    j = 0
    n = len(s)
    count = 0

    while i < n:
        j = i + 2
        if j < n:
            if s[j].isupper():
                count += 1
        i += 2

    return count
