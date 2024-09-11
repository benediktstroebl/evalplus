```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case characters.
    """
    # Initialize sum to 0
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

In this script, we use the `ord()` function to get the ASCII code of each character. The `isupper()` method is used to check if a character is upper case. The sum of the ASCII codes of the upper case characters is calculated and returned.