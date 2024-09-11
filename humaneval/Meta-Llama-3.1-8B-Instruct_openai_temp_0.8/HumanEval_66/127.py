```python
def digitSum(s):
    """
    This function calculates the sum of the ASCII codes of the upper case characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of the ASCII codes of the upper case characters.
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

This script defines a function `digitSum` that takes a string `s` as input. It uses a generator expression within the built-in `sum` function to calculate the sum of the ASCII codes of the upper case characters in the string. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to check if a character is upper case. The script then includes test cases to verify that the function works correctly.