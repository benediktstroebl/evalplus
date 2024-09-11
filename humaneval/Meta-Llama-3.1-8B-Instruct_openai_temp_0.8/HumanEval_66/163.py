```python
def digitSum(s):
    """Returns the sum of the upper characters only ASCII codes."""
    
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add the ASCII value of the character to the total sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that calculates the sum of ASCII codes of only upper-case characters in a given string. It uses the `ord` function to get the ASCII value of each character and the `isupper` method to check if a character is an uppercase letter. The total sum is then returned by the function.