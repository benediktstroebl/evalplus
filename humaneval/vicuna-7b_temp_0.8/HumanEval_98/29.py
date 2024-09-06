
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # initialize the count to 0
    count = 0
    
    # loop through the characters in s
    for i, c in enumerate(s):
        # if the character is an uppercase vowel, add 1 to the count
        if c.upper() in 'AEIO':
            count += 1
    
    return count