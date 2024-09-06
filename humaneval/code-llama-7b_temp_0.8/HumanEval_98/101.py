
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Initialize count to 0
    count = 0

    # Loop through each index in s
    for i in range(0, len(s), 2):
        # Check if current character is uppercase
        if s[i].isupper():
            # Increment count
            count += 1

    # Return count
    return count
