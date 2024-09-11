```python
def digitSum(s):
    """Returns the sum of the upper characters only ASCII codes."""
    
    # Initialize the sum to 0
    total = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add the ASCII code of the character to the total
            total += ord(char)
    
    # Return the total sum
    return total

# Test the function with examples
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines a function `digitSum` that calculates the sum of the ASCII codes of upper-case characters in a given string. It uses the `ord` function to get the ASCII code of each character and the `isupper` method to check if a character is an upper-case letter. The script then tests the function with the provided examples.