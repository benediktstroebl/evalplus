
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    
    # Initialize a counter to 0
    count = 0
    
    # Iterate through the string and count the number of uppercase vowels
    for i in range(len(s)):
        if s[i].isupper():
            if i % 2 == 0:
                count += 1
        
    return count