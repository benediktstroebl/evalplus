```python
def digitSum(s):
    """
    This function calculates the sum of ASCII values of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII values of upper case characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines a function `digitSum` that takes a string `s` as input. It uses a generator expression to iterate over each character `c` in the string, and checks if the character is an upper case letter using the `isupper` method. If it is, the ASCII value of the character is calculated using the `ord` function, and added to the sum. The function returns the total sum.

The test cases at the end of the script demonstrate the function's usage and expected output.