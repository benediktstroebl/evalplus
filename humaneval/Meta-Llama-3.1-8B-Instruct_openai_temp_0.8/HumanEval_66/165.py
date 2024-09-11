```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of uppercase characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of uppercase characters.
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

This Python script defines the `digitSum` function, which calculates the sum of ASCII codes of uppercase characters in a given string. It uses a generator expression to iterate over the characters in the string, filters out lowercase characters using the `isupper` method, and calculates the ASCII code of each character using the `ord` function. The sum of these ASCII codes is then returned. The test cases at the end of the script demonstrate the function's usage.