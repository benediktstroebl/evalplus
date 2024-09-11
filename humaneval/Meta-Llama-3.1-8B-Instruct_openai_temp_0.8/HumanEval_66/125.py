```python
def digitSum(s):
    """
    Returns the sum of ASCII codes of upper characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper characters.

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

This script defines a function `digitSum` that uses a generator expression to iterate over each character `c` in the input string `s`. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to check if the character is uppercase. The `sum` function is then used to calculate the sum of the ASCII codes of the uppercase characters.