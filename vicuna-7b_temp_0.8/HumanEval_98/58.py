
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    n = len(s)
    for i in range(n//2):
        if s[i] == chr(ord('A') - 32 + 1) or s[i] == chr(ord('E') - 32 + 1) or s[i] == chr(ord('I') - 32 + 1) or s[i] == chr(ord('O') - 32 + 1) or s[i] == chr(ord('U') - 32 + 1):
            return 1
    return 0