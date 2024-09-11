```python
def digitSum(s):
    """
    Returns the sum of the ASCII codes of upper characters in a given string.

    Args:
        s (str): Input string.

    Returns:
        int: Sum of ASCII codes of upper characters.
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

This script defines a function `digitSum` that takes a string `s` as input. It uses a generator expression to iterate over each character `c` in the string, and checks if it's an uppercase letter using the `isupper` method. If it is, the ASCII code of the character is calculated using the `ord` function and added to the sum. The function returns the total sum of the ASCII codes of the uppercase characters in the string. The test cases at the end verify that the function works correctly.