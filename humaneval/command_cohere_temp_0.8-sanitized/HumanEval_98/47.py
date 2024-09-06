def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels to be counted
    vowels = 'AEIOU'
    
    # Initialize the count to zero
    count = 0
    
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Check if the character is uppercase and a vowel
        if char.isupper() and char in vowels:
            # If the index is even, increment the count
            if i % 2 == 0:
                count += 1
    
    # Return the final count
    return count