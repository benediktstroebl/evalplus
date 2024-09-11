```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII codes of upper case characters.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that takes a string `s` as input and returns the sum of ASCII codes of upper case characters in the string. It uses a generator expression to iterate over the characters in the string, and the `ord` function to get the ASCII code of each character. The `isupper` method is used to filter out non-upper case characters. The sum of the ASCII codes is calculated using the `sum` function. The test cases at the end demonstrate the function's behavior with various inputs.