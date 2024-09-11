```python
def digitSum(s):
    """
    Returns the sum of the upper characters only' ASCII codes in the given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper characters only' ASCII codes.
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

This script defines a function `digitSum` that calculates the sum of the ASCII codes of only the upper case characters in the input string `s`. It uses a generator expression to iterate over the characters in `s` and the `ord` function to get their ASCII codes. The `isupper` method is used to filter out lower case characters. The `sum` function is then used to calculate the sum of these ASCII codes.