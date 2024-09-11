```python
def digitSum(s):
    """Returns the sum of the ASCII codes of upper case characters in a string."""
    
    # Initialize a variable to store the sum of ASCII codes
    ascii_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an upper case letter
        if char.isupper():
            # Add the ASCII code of the character to the sum
            ascii_sum += ord(char)
    
    # Return the sum of ASCII codes
    return ascii_sum

# Test the function with examples
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script uses a simple loop to iterate over each character in the input string. It checks if the character is an upper case letter using the `isupper()` method, and if so, it adds the ASCII code of the character to the `ascii_sum` variable using the `ord()` function. Finally, it returns the sum of ASCII codes.