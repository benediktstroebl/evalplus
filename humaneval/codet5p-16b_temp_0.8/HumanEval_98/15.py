
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    
    if s is None or len(s) == 0:
        return 0
    
    result = 0
    for idx in range(0, len(s), 2):
        if s[idx].isupper():
            if s[idx + 1].lower() in 'aeiou':
                result += 1
        
    return result
    
    
