```python
def digitSum(s):
    """
    Returns the sum of the ASCII codes of the upper case characters in a string.

    Parameters:
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

This script defines a function `digitSum` that calculates the sum of the ASCII codes of the upper case characters in a string. It uses a generator expression to iterate over the characters in the string, filters out the lower case characters using the `isupper` method, and uses the `ord` function to get the ASCII code of each character. The `sum` function is then used to calculate the total sum. The script also includes test cases to demonstrate the correctness of the function.