
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Get length of string
    n = len(s)
    
    # Initialize result with 0
    r = 0
    
    # Loop through each character
    for i in range(n):
        # If current character is uppercase vowel
        if s[i].isupper():
            r += 1
        
    return r