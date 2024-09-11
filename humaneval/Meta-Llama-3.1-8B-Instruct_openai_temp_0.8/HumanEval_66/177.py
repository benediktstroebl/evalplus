```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of upper case characters.
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

In this script, the `isupper()` method is used to check if a character is upper case. The `ord()` function is used to get the ASCII code of a character. The `sum()` function is used to calculate the sum of the ASCII codes of upper case characters. The function is then tested with the provided test cases.