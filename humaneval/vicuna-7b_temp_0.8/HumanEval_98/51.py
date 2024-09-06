
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s = s.upper()
    result = 0
    for i in range(len(s)-1):
        if s[i+1] == s[i] and s[i] == chr(ord('A')+i//2):
            result += 1
    return result
