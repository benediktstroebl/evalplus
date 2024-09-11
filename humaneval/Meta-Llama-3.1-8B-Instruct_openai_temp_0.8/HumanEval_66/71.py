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
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that takes a string `s` as input. It uses a generator expression to iterate over each character `c` in the string. The `isupper` method checks if the character is an uppercase letter, and the `ord` function returns the ASCII code of the character. If the character is uppercase, its ASCII code is added to the sum. The `sum` function is used to calculate the total sum of the ASCII codes.