
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    if s == "":
        return 0
    if len(s) % 2 == 1:
        return s[0].upper() in "AEIOU" and count_upper(s[1:])
    return s[0].upper() in "AEIOU" + s[1].upper() and count_upper(s[2:])
    
