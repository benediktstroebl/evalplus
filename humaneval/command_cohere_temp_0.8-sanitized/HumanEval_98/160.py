def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Declare the count for the uppercase vowels in even indices
    count = 0
    # Initialize the string to be checked
    s = s.strip()
    # Use a for loop and the string's length to iterate through each possible index
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU' and s[i].isupper():
            count += 1
    return count