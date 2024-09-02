
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j] and s[i] == ord('A'):
            i += 1
            j -= 1
        elif s[i] == s[j] and s[i] == ord('E'):
            i += 1
            j -= 1
        elif s[i] == s[j] and s[i] == ord('I'):
            i += 1
            j -= 1
        elif s[i] == s[j] and s[i] == ord('O'):
            i += 1
            j -= 1
        elif s[i] == s[j] and s[i] == ord('U'):
            i += 1
            j -= 1
        else:
            if s[i] != s[j]:
                break
            i += 1
            j -= 1
    return i