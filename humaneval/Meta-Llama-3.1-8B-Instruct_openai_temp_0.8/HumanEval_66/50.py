```python
def digitSum(s):
    """
    This function calculates the sum of ASCII values of uppercase characters in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of ASCII values of uppercase characters.
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

Explanation:
- The `ord()` function is used to get the ASCII value of a character.
- `isupper()` method returns `True` if all characters in the string are uppercase, otherwise it returns `False`.
- The `sum()` function adds up the ASCII values of the uppercase characters.

This script defines a function `digitSum()` that takes a string as input and returns the sum of ASCII values of its uppercase characters. It includes test cases to verify its correctness.