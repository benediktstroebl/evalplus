```python
def digitSum(s):
    """Returns the sum of the upper characters in the string s."""
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script uses a generator expression to iterate over each character `c` in the string `s`, checks if the character is upper case using the `isupper()` method, and sums up the ASCII values of the upper case characters using `ord(c)`. The result is returned by the `sum()` function.