```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of all uppercase characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of uppercase characters.
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

This script includes a function `digitSum` that calculates the sum of ASCII codes of all uppercase characters in a string. It uses a generator expression within the `sum` function to iterate over the characters in the string, and the `isupper` method to filter out lowercase characters. The `ord` function is used to get the ASCII code of each character. The test cases are included at the end to verify the function's correctness.