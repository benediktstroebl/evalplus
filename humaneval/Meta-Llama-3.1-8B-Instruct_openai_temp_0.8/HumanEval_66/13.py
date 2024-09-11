```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII values of uppercase characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the ASCII values of uppercase characters.

    Examples:
        >>> digitSum("")
        0
        >>> digitSum("abAB")
        131
        >>> digitSum("abcCd")
        67
        >>> digitSum("helloE")
        69
        >>> digitSum("woArBld")
        131
        >>> digitSum("aAaaaXa")
        153
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

In this script, we define a function `digitSum` that calculates the sum of the ASCII values of uppercase characters in the input string `s`. We use a generator expression to iterate over the characters in the string and the `isupper` method to check if each character is uppercase. The `ord` function is used to get the ASCII value of each character. The sum of these ASCII values is then returned by the function.

The test cases at the end of the script demonstrate the function's behavior with various inputs.