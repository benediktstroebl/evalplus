```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper characters only ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    # Initialize the sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Add the ASCII value of the character to the sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test the function
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of the upper characters only ASCII codes. It initializes a variable `total_sum` to 0 and then iterates over each character in the string. If the character is an uppercase letter, it adds the ASCII value of the character to `total_sum`. Finally, it returns `total_sum`. The script then tests the function with the provided examples.