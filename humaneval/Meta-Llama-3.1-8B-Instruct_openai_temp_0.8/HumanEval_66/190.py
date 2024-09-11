```python
def digitSum(s):
    """
    This function takes a string as input and returns the sum of the upper characters only ASCII codes.

    Parameters:
    s (str): The input string

    Returns:
    int: The sum of the upper characters only ASCII codes
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

This script defines a function `digitSum` that takes a string `s` as input. The function uses a generator expression to iterate over each character `c` in the string `s`. The `isupper` method is used to check if a character is upper case. If it is, the `ord` function is used to get its ASCII code, which is then added to the sum using the `sum` function. The result is returned by the function.

The test cases at the end of the script demonstrate the function's behavior with different input strings.