```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case letters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case letters in the string.

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
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

In this script, the `digitSum` function uses a generator expression to iterate over each character in the string. The `ord` function is used to get the ASCII code of each character. The `isupper` method is used to check if a character is an uppercase letter. The `sum` function is then used to calculate the sum of the ASCII codes of all uppercase letters in the string.