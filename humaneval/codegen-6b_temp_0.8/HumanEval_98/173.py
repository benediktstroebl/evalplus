
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    v_count = 0
    for i in range(0, len(s), 2):
        c = s[i].lower()
        if c in 'aeiou':
            v_count += 1
    return v_count
