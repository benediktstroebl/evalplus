
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    counter = 0
    for char in s:
        if char.upper() == char:
            counter += 1
        if counter % 2 == 0:
            counter = 0
    return counter
