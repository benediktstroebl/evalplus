```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of upper characters ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())

# Example usage:
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

In this script, the `ord()` function is used to get the ASCII code of each character, and the `isupper()` method is used to filter out lower case characters. The `sum()` function is then used to calculate the sum of the ASCII codes of the upper case characters.