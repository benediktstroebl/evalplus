```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of only uppercase characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of uppercase characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script uses a generator expression within the built-in `sum` function to efficiently calculate the sum of ASCII codes of uppercase characters in the input string. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to check if a character is uppercase.