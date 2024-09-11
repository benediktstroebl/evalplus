```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper characters only ASCII codes.
    """
    # Use a generator expression to iterate over each character in the string
    # Use the isupper() method to check if the character is uppercase
    # Use the ord() function to get the ASCII code of the character
    # Add up all the ASCII codes using the sum() function
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines a function `digitSum` that takes a string `s` as input, iterates over each character using a generator expression, checks if the character is uppercase using the `isupper()` method, gets the ASCII code of the character using the `ord()` function, and adds up all the ASCII codes using the `sum()` function. The test cases at the end of the script demonstrate the function's behavior with different inputs.