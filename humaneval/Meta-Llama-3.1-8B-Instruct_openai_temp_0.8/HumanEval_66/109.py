```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a string.

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

In this script, the function `digitSum` uses a generator expression to iterate over each character `c` in the string `s`. It checks if `c` is an upper case character using the `isupper` method. If it is, it calculates the ASCII code of `c` using the `ord` function and adds it to the sum. The sum is then returned.