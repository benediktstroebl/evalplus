
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s = s.lower()
    uppers = 0
    for index in range(0,len(s),2):
        if s[index] in "aeiou":
            uppers += 1
    return uppers
