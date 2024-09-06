def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Define the uppercase vowels
    v = 'AEIOU'
    # Initialize the count to 0
    count = 0
    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the current character is in the uppercase vowel set and if its index is even
        if char.isupper() and char in v and i % 2 == 0:
            # If true, increment the count by 1
            count += 1
    # Return the final count
    return count