```python
def digitSum(s):
    """
    Returns the sum of the upper characters only' ASCII codes in the given string.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the upper characters only' ASCII codes.
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

In this script, the `digitSum` function uses a generator expression to iterate over each character `c` in the string `s`. It checks if `c` is an uppercase letter using the `isupper` method, and if so, it adds the ASCII code of `c` (obtained using the `ord` function) to the sum. Finally, it returns the sum. The script includes the test cases provided in the problem statement.