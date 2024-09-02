
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    s = s.lower()
    for i,c in enumerate(s):
        if i % 2 == 0 and c in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count
