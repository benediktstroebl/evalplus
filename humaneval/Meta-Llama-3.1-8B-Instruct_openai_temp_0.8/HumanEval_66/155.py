```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of only the upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Should return 0
print(digitSum("abAB"))  # Should return 131
print(digitSum("abcCd"))  # Should return 67
print(digitSum("helloE"))  # Should return 69
print(digitSum("woArBld"))  # Should return 131
print(digitSum("aAaaaXa"))  # Should return 153
```

This script uses a generator expression within the built-in `sum` function to calculate the sum of ASCII codes of upper case characters. The `ord` function returns the ASCII value of a character, and the `isupper` method checks if a character is upper case.