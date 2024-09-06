def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    num = 0
    for i, char in enumerate(s):
        if i % 2 == 0 and char.isupper() and char in 'AEIOU':
            num += 1
    return num