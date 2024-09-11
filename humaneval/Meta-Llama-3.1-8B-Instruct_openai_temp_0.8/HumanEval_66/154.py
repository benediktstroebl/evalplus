```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case letters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case letters.
    """
    # Initialize the sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is an upper case letter
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

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of the ASCII codes of the upper case letters in the string. The `isupper` method is used to check if a character is an upper case letter, and the `ord` function is used to get the ASCII code of a character. The script also includes test cases to verify the correctness of the function.