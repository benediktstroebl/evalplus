def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels
    vowels = 'AEIOU'
    # Initialize the count of uppercase vowels in even indices
    count = 0
    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the current character is an uppercase vowel
        if char.isupper() and char in vowels and (i + 1) % 2 == 0:
            count += 1
    # Return the count of uppercase vowels in even indices
    return count