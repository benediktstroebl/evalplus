```python
def digitSum(s):
    """
    This function calculates the sum of ASCII values of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII values of upper case characters.
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