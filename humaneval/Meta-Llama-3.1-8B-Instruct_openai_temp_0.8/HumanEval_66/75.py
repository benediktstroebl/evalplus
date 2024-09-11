```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of uppercase characters in a given string.

    Parameters:
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

In this script, the `ord` function is used to get the ASCII value of each character, and the generator expression `for c in s if c.isupper()` is used to filter out the upper case characters. The `sum` function then adds up these ASCII values.