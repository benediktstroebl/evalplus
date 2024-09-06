def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels to be counted
    vowels = 'AEIOU'
    
    # Initialize the count to 0
    count = 0
    
    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the current character is uppercase and a vowel
        if char.isupper() and char in vowels:
            # Check if the index is even and increment the count if it is
            if i % 2 == 0:
                count += 1
    # Return the count of uppercase vowels in even indices
    return count