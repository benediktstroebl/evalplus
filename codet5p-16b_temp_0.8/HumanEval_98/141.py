
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """

    
    upper_count = 0
    index = 1
    for character in s:
        if character.isupper():
            if index % 2 == 0:
                upper_count += 1
        index += 1
        
    return upper_count
        
        
        
