
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s = s.upper()
    n = len(s)
    count = 0
    i = n // 2
    for i in range(n - 1, -1, -1):
        if s[i] == s[i + 1] and s[i] == chr(ord('A') - 1 + (n // 2 % 2)):
            count += 1
        i -= 1
    return count
