```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper characters.
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

Explanation:

- The `ord()` function returns the Unicode code point for the given character.
- The `isupper()` function returns `True` if the character is an uppercase letter, and `False` otherwise.
- The `sum()` function adds up all the ASCII codes of the upper characters.
- The generator expression `(ord(c) for c in s if c.isupper())` generates ASCII codes for upper characters in the string.
- The `for` loop iterates over each character in the string.