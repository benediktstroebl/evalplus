
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    if len(s) < 2:
        return 0
    
    s = s.lower()
    count = 0
    for (index, char) in enumerate(s):
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            if index % 2 == 0:
                count += 1
            
    return count
