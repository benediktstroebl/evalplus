```python
def digitSum(s):
    """Returns the sum of the upper ASCII codes in the given string."""
    
    # Initialize a variable to store the sum of upper ASCII codes
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Add the ASCII code of the character to the total sum
            total_sum += ord(char)
    
    # Return the total sum of upper ASCII codes
    return total_sum

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script uses the built-in `ord` function to get the ASCII code of each character, and the `isupper` method to check if a character is uppercase. It iterates over each character in the string and adds its ASCII code to the total sum if it's uppercase. The function then returns the total sum of upper ASCII codes.