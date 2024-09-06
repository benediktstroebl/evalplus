def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Ensure the string contains at least one character
    if not s:
        return 0
    
    # List of uppercase vowels
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    # Initialize the count of uppercase vowels in even positions
    count = 0
    
    # Iterate through each character in the string
    for i, char in enumerate(s):
        if char.isupper() and char in vowels and (i % 2 == 0):
            count += 1
    
    return count