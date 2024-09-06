
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    count = 0
    vowels = "AEIOU"
    
    for c in s:
        for index, v in enumerate(vowels):
            if c == v and (index % 2 == 0):
                count += 1
    
    return count
