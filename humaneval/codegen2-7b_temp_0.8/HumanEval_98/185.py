
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    if s[0] == "a" or s[0] == "e" or s[0] == "i" or s[0] == "o" or s[0] == "u":
        return 1
    else:
        return 0
