```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test the function with the provided examples
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

Explanation:
- The `ord(c)` function is used to get the ASCII value of each character in the string.
- The `isupper()` method is used to check if a character is an uppercase letter.
- The `sum()` function is used to calculate the total sum of ASCII values of all uppercase characters.