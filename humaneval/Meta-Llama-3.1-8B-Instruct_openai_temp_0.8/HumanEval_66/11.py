```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of upper case characters in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The sum of ASCII codes of upper case characters in the string.
    """
    # Initialize the sum variable to 0
    total = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an upper case letter
        if char.isupper():
            # Add the ASCII code of the character to the total
            total += ord(char)
    
    # Return the total sum
    return total

# Test cases
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

This script defines a function `digitSum` that takes a string as input, calculates the sum of ASCII codes of upper case characters, and returns the result. The function uses the `isupper` method to check if a character is an upper case letter and the `ord` function to get the ASCII code of a character. The script also includes test cases to verify the function's correctness.