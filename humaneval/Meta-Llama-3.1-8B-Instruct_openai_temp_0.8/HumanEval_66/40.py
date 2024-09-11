```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of only upper case characters in a given string.

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
            # Add the ASCII value of the character to the sum
            total_sum += ord(char)
    
    # Return the total sum
    return total_sum

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines a function `digitSum` that calculates the sum of ASCII codes of only upper case characters in a given string. It iterates over each character in the string, checks if it is upper case using the `isupper` method, and adds its ASCII value (obtained using the `ord` function) to the total sum. The function returns the total sum. The script also includes test cases to verify the correctness of the function.