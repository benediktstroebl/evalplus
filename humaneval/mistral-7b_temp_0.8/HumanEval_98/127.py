
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    upper = 0
    for index, ch in enumerate(s):
        if ch.isupper() and index % 2 == 0:
            upper += 1
    return upper
