
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = 'aeiouAEIOU'
    n = len(s) // 2
    count = 0
    for i in range(n):
        if s[i] in vowels:
            count += 1
    return count
