Here's a Python function that solves the problem:
```python
def digitSum(s):
    """
    Returns the sum of the ASCII codes of the upper characters in the input string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII codes of the upper characters.

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
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```
This code uses a generator expression to iterate over the characters in the string, checking if each character is an uppercase letter using the `isupper()` method. If it is, the `ord()` function is used to get its ASCII code, and the result is included in the sum.