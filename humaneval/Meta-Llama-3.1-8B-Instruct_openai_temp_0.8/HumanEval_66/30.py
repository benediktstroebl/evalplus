```python
def digitSum(s):
    """
    This function calculates the sum of ASCII values of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII values of upper case characters.

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

# Test the function
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This function uses a generator expression to iterate over each character `c` in the input string `s`. The `ord(c)` function is used to get the ASCII value of each character. The `isupper()` function is used to check if a character is upper case, and the `sum` function is used to add up the ASCII values of the upper case characters.