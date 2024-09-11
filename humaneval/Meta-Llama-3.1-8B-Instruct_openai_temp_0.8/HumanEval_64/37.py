### Vowels Count Function
```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string. 
    It considers 'y' as a vowel only when it's at the end of the string.
    
    Args:
    s (str): The input string.
    
    Returns:
    int: The count of vowels in the string.
    """
    
    # Initialize count of vowels
    count = 0
    
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If 'y' is at the end, increment count by 1
            count += 1
        
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel
            if char in 'aeiou':
                # If it's a vowel, increment count by 1
                count += 1
    
    # Return the count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("AEIOU"))  # Expected output: 5
print(vowels_count("bcd"))    # Expected output: 0
print(vowels_count("y"))      # Expected output: 1
```
This script defines a function `vowels_count` that takes a string `s` as input and returns the count of vowels in the string. It considers 'y' as a vowel only when it's at the end of the string. The script includes test cases to demonstrate the function's correctness.