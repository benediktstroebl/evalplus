
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # check if s is empty or a single digit
    if len(s) == 1 or s == '0':
        return 0
    vowel_count = 0
    i = 0
    for j in range(len(s)):
        if s[j] == s[i] and s[j] == chr(ord(s[i]) + 1):
            i += 1
        elif s[j] == '0':
            vowel_count += 1
        j += 1
    return vowel_count // 2