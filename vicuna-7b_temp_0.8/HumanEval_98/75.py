
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s = s.upper()
    if s[0] == s[-1]:
        return 0
    n = len(s)
    count = 0
    for i in range(n//2):
        if s[i] == s[n-i-1] == 'A':
            count += 1
        elif s[i] == s[n-i-1] == 'B':
            count += 1
        elif s[i] == s[n-i-1] == 'C':
            count += 1
        elif s[i] == s[n-i-1] == 'D':
            count += 1
        elif s[i] == s[n-i-1] == 'E':
            count += 1
        else:
            break
    return count
