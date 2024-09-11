```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string. 'y' is a vowel only at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lower case for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Initialize a flag to check if 'y' is at the end of the string
    is_y_at_end = False
    
    # Check if the string ends with 'y'
    if s.endswith('y'):
        # If it does, remove the last character ('y') and set the flag
        s = s[:-1]
        is_y_at_end = True
    
    # Count the vowels
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            count += 1
    
    # If 'y' was at the end of the string, add 1 to the count
    if is_y_at_end:
        count += 1
    
    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```