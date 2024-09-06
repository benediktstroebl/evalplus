def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Define the vowels to check
    vowels = set(['A', 'E', 'I', 'O', 'U'])
    # Initialize the count to zero
    count = 0
    # Iterate through the string
    for i in range(0, len(s), 2):
        if s[i].isupper() and s[i] in vowels:
            count += 1
    return count