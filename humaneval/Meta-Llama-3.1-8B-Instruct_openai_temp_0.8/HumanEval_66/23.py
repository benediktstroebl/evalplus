```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the upper characters only ASCII codes.
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

This script defines the function `digitSum` that takes a string `s` as input and returns the sum of the upper characters only ASCII codes using a generator expression and the built-in `ord` function to get the ASCII code of each character. The `isupper` method is used to filter out the upper characters. The test cases are included at the end to verify the correctness of the function.