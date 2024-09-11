```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case characters.

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

This script defines a function `digitSum` that calculates the sum of ASCII codes of upper case characters in a given string. It uses a generator expression to iterate over the characters in the string, checks if each character is an upper case letter using the `isupper` method, and uses the `ord` function to get the ASCII code of each character. The sum of these ASCII codes is then returned.