
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s = s.upper()  # convert to uppercase
    i = 0
    n = len(s)
    while i < n//2:
        if s[i] == 'B':
            if s[i+1] == 'B':
                i += 2
            elif s[i+1] == 'C':
                i += 1
            elif s[i+1] == 'D':
                i += 2
        else:
            if s[i+1] == 'D':
                i += 1
            elif s[i+1] == 'E':
                i += 2
    return i - n // 2
