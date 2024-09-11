```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case characters.
    """
    # Initialize the sum to 0
    total_sum = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is upper case
        if char.isupper():
            # Add the ASCII value of the character to the sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test the function with examples
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines a function `digitSum` that calculates the sum of ASCII codes of upper case characters in a given string. The function uses the `ord` function to get the ASCII value of each character and the `isupper` method to check if a character is upper case. The script then tests the function with the provided examples.