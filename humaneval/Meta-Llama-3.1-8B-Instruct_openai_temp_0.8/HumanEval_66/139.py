```python
def digitSum(s):
    """
    This function takes a string as input, filters out the uppercase characters and returns their sum of ASCII values.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII values of uppercase characters in the string.
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

This script defines a function `digitSum` that takes a string `s` as input. It uses a generator expression to iterate over each character `c` in the string, filters out the ones that are not uppercase using the `isupper` method, and calculates the sum of their ASCII values using the `ord` function. The result is then returned by the function. The test cases at the end demonstrate the function's behavior with various inputs.