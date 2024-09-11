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

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

In this script, the `digitSum` function uses a generator expression to iterate over each character in the input string. It checks if the character is an upper case letter using the `isupper` method, and if so, adds its ASCII code (calculated using `ord`) to the sum. The `ord` function returns the ASCII value of a character, and `isupper` returns `True` if the character is an upper case letter and `False` otherwise.