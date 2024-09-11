```python
def digitSum(s):
    """
    Returns the sum of upper ASCII codes in the input string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of upper ASCII codes.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of the ASCII codes of the upper-case characters in the string. The `ord` function is used to get the ASCII code of a character, and the `isupper` method is used to check if a character is upper-case. The `sum` function is used to calculate the sum of the ASCII codes. The test cases at the end of the script demonstrate the function's behavior.