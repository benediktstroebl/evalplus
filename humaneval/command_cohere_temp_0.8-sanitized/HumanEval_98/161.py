def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Ensure the string contains at least one character
    if not s:
        return 0
    
    # Declare variable to store the result
    count = 0
    
    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Check if the character is an uppercase vowel
        if char.isupper() and char in 'AEIOU':
            # Check if the index is even
            if i % 2 == 0:
                count += 1
    
    # Return the final count
    return count