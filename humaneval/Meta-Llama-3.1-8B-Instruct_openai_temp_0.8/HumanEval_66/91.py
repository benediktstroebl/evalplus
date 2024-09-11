```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of upper characters ASCII codes.
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

This script defines a function `digitSum` that takes a string `s` as input. It uses a generator expression to iterate over each character in the string, checks if the character is uppercase using the `isupper` method, and if so, adds its ASCII code (obtained using the `ord` function) to the sum. The result is then returned. The function is tested with the provided examples.