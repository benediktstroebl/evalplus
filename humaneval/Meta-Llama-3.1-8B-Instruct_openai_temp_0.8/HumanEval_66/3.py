```python
def digitSum(s):
    """
    This function calculates the sum of upper case ASCII codes in a given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of upper case ASCII codes.
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

In this script, the `digitSum` function uses a generator expression to iterate over each character `c` in the string `s`. It uses the `isupper` method to check if a character is upper case, and if so, it uses the `ord` function to get the ASCII code of the character. The `sum` function then adds up these ASCII codes. The test cases at the end of the script demonstrate the function's correctness.