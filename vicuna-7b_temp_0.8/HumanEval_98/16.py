
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = 'aeiouAEIOU'
    i = 0
    while i < len(s):
        if s[i] in vowels and s[i+1] in vowels:
            i += 1
        elif s[i] == s[i+1] and s[i] in vowels and s[i+1] == 'n':
            i += 1
        i += 1
    return i - 1
