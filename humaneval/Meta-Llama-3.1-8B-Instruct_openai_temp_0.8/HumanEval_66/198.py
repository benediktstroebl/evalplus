```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of upper case characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII codes of upper case characters in the string.
    """
    return sum(ord(c) for c in s if c.isupper())


# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

This script defines a function `digitSum` that calculates the sum of the ASCII codes of upper case characters in a given string. It uses a generator expression to iterate over each character in the string, checks if the character is upper case using the `isupper` method, and sums up the ASCII codes using the `ord` function. The result is then returned by the function. The test cases at the end of the script verify that the function behaves correctly for the examples provided.