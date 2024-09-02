
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Split string into list of characters
    li=list(s)
    count = 0
    for i in range(0, len(li), 2):
        if li[i].isupper():
            count += 1
    return count
