
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    if len(s) == 0:
        return 0
    
    vowels = "AEIOU"
    count = 0
    
    for index in range(0, len(s), 2):
        if s[index] in vowels and s[index].isupper():
            count += 1
    
    return count
