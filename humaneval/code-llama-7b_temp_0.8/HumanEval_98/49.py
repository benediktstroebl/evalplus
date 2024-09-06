
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Initialize count and index
    count = 0
    i = 0
    
    # Loop through characters in string s
    while i < len(s):
        # Check if the character at index i is an uppercase vowel
        if s[i].upper() in ['A','E','I','O','U']:
            # Check if index i is even
            if i % 2 == 0:
                # Add one to count
                count += 1
        # Increment index
        i += 1
        
    # Return count
    return count
