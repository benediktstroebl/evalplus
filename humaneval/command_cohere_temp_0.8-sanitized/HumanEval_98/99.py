def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels to consider
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    
    # Initialize the count to zero
    count = 0
    
    # Iterate through the string
    for char in s:
        if char.isupper() and char in vowels and (len(s) % 2 == 0):
            count += 1
    
    return count