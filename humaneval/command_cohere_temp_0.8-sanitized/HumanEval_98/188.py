def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    # Initialize the count to 0
    count = 0
    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the character is an uppercase vowel and if its index is even
        if char.isupper() and char in vowels and (i % 2 == 0):
            count += 1
    # Return the count of uppercase vowels in even indices
    return count