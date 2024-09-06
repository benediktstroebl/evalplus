
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Define the string s
    s = list(s)
    # Create an empty list to store the count
    count = []
    # Loop through the characters of the string
    for i in range(len(s)):
        # If the character is an uppercase vowel, increment the count
        if s[i] in 'aeiouAEIOU':
            count.append(count.count(s[i]))
    # Return the count
    return count
