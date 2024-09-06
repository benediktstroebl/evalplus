def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    # Ensure the string contains at least one character
    if not s:
        return 0
    
    # List of uppercase vowels
    vowels = 'AEIOU'
    
    # Initialize count
    count = 0
    
    # Iterate through the string
    for i in range(len(s)):
        if i % 2 == 0 and s[i] in vowels and s[i].isupper():
            count += 1
    
    return count