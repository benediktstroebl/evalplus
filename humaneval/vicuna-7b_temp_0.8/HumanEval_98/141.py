
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    num_vowels = len(s)
    count = 0
    for i in range(num_vowels // 2, num_vowels):
        if s[i] == s[i-1] == 'a' or s[i] == s[i-1] == 'E' or s[i] == s[i-1] == 'i':
            count += 1
    return count
