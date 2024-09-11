```python
def digitSum(s):
    """Returns the sum of the upper characters only' ASCII codes in the string s."""
    
    # Initialize sum as 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is upper case
        if char.isupper():
            # Add the ASCII code of the character to the sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test cases
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

This script works by iterating over each character in the string `s`. If the character is upper case, it adds the ASCII code of the character to the total sum. The ASCII code of a character can be obtained using the `ord` function. The sum of the ASCII codes of the upper case characters is then returned.