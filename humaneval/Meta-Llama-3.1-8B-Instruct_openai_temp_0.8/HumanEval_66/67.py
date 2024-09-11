```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of the upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the ASCII codes of the upper case characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test the function with examples
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```

In this script, the `digitSum` function uses a generator expression within the `sum` function to iterate over the characters in the string `s`. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to check if a character is upper case. The sum of the ASCII codes of the upper case characters is then returned.