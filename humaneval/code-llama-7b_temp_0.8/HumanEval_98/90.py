
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Initialize a count to zero
    count = 0
    # Iterate through s
    for i in range(len(s)):
        # If s[i] is an uppercase vowel and i is an even number
        if s[i].isupper() and (i % 2 == 0):
            # Increment count
            count += 1
    # Return count
    return count

