
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    l = len(s)
    count = 0
    for i in range(l//2):
        if s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            count += 1
    return count
