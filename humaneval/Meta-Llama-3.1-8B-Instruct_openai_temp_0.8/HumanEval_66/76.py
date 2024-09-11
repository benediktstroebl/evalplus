```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the ASCII codes of upper case characters.
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

In this script, the `digitSum` function uses a generator expression to iterate over each character in the input string `s`. The `isupper` method checks if a character is upper case. If it is, the `ord` function is used to get its ASCII code, and this code is added to the sum. If the character is not upper case, it is skipped. The sum of the ASCII codes of all upper case characters is then returned.