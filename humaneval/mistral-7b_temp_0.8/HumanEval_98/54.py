
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    u_count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOUaeiou':
            if s[i].isupper():
                u_count += 1
    return u_count
