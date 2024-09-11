```python
def digitSum(s):
    """
    Returns the sum of the ASCII codes of the upper case characters in the input string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the ASCII codes of the upper case characters.

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

In this script, the `digitSum` function uses a generator expression to iterate over the characters in the input string `s`. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to check if the character is an upper case letter. The `sum` function is then used to add up the ASCII codes of the upper case characters.