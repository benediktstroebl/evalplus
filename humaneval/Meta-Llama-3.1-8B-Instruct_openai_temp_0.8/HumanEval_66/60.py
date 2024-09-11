```python
def digitSum(s):
    """Returns the sum of upper ASCII codes in the input string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of upper ASCII codes in the input string.
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

This script uses a generator expression to iterate over each character `c` in the input string `s`. The `ord` function returns the ASCII code of `c`, and `isupper` checks if `c` is an uppercase letter. The `sum` function then adds up the ASCII codes of all uppercase characters.