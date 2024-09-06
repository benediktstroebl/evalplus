
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    if s:
        if s[0].isupper():
            if s[0] in 'AEIOU':
                count += 1
    for i in range(1, len(s), 2):
        if s[i].isupper():
            if s[i] in 'AEIOU':
                count += 1
    return count
