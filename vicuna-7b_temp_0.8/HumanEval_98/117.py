
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    num = 0
    for i in range(len(s)-1):
        if s[i] == s[i+2] and s[i] == chr(ord('A') + 1) or s[i] == chr(ord('E') + 1) or s[i] == chr(ord('I') + 1) or s[i] == chr(ord('O') + 1) or s[i] == chr(ord('U') + 1):
            num += 1
    return num
