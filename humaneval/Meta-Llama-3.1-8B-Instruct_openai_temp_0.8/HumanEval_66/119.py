```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes for uppercase characters in a given string.

    Args:
        s (str): Input string.

    Returns:
        int: Sum of ASCII codes for uppercase characters.

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
    return sum(ord(char) for char in s if char.isupper())

# Test the function
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

In this script, the `ord` function is used to get the ASCII code of each character in the string, and the `isupper` function is used to check if a character is uppercase. The `sum` function is then used to calculate the sum of ASCII codes for uppercase characters.