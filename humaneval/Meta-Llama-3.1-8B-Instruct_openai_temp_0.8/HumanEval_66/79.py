```python
def digitSum(s):
    """
    This function calculates the sum of ASCII codes of upper case characters in a given string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The sum of ASCII codes of upper case characters in the string.
    """
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

In this script, the `digitSum` function uses a generator expression to iterate over each character `c` in the string `s`. The `isupper` method is used to check if `c` is an upper case character. If it is, the ASCII code of `c` is calculated using the `ord` function and added to the sum. The `sum` function is then used to calculate the total sum of ASCII codes.