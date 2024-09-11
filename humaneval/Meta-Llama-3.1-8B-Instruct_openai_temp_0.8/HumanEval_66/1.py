**Digit Sum Function**
======================

The following Python script defines a function `digitSum` that calculates the sum of ASCII codes of upper case characters in a given string.

```python
def digitSum(s):
    """
    Returns the sum of ASCII codes of upper case characters in a given string.

    Args:
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

This script uses the `ord` function to get the ASCII code of each character and the `isupper` method to filter out lower case characters. The `sum` function is then used to calculate the sum of the ASCII codes of the upper case characters.