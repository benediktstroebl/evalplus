def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels to be counted
    vowels = 'AEIOU'
    # Initialize the count to 0
    count = 0
    # Loop through each character in the string
    for i in range(len(s)):
        if s[i] in vowels and (i+1) % 2 == 0:
            if s[i].isupper():
                count += 1
    # Return the count of uppercase vowels in even indices
    return count