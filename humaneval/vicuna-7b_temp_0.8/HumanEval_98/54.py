
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Get the string
    s = s.upper()
    
    # Get the length of the string
    n = len(s)
    
    # Initialize a 0-indexed array
    vowels = [0] * n
    
    # Iterate through the string
    for i in range(n):
        if s[i] == 'B':
            vowels[i] += 1
            if vowels[i] % 2 == 0:
                vowels[i] += 1
    
    return vowels[::-1].count('0')
