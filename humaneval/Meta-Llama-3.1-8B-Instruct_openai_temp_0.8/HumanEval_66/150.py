```python
def digitSum(s):
    """
    Returns the sum of the upper characters only ASCII codes in the given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of upper characters only ASCII codes.
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

This script defines a function `digitSum` that takes a string `s` as input, uses a generator expression to iterate over the characters in `s`, checks if each character is uppercase using the `isupper` method, converts each uppercase character to its ASCII code using the `ord` function, and sums up these ASCII codes using the `sum` function. The result is then returned by the function.

The test cases at the end of the script demonstrate the function's behavior on different inputs.