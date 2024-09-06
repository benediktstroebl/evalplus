
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    if len(s) % 2 == 0:
        vowels = set(string.ascii_uppercase)
        for i in range(len(s)):
            if s[i] in vowels and s[i+1] in vowels:
                vowels.remove(s[i])
                vowels.remove(s[i+1])
                return 1
        return 0
    else:
        return -1
