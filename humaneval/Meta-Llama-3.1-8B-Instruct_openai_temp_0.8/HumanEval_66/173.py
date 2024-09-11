```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper characters only ASCII codes.
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

This Python function uses a generator expression inside the built-in `sum` function to iterate over each character `c` in the string `s`. The `ord` function is used to get the ASCII code of each character. The `if c.isupper()` condition filters out lower-case characters. The result is the sum of the ASCII codes of the upper-case characters in the string.