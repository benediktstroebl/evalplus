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

# Test the function
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of the ASCII codes of the upper-case characters in the string. It uses a generator expression to iterate over the string, and the `isupper` method to check if a character is upper-case. The `ord` function is used to get the ASCII code of each character. The `sum` function is then used to add up the ASCII codes of the upper-case characters.