```python
def digitSum(s):
    """Returns the sum of the upper characters only ASCII codes in a string."""
    return sum(ord(c) for c in s if c.isupper())

# Test the function
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that takes a string `s` as input, uses a generator expression to iterate over each character in the string, and adds the ASCII code of each upper-case character to the sum. The `ord` function is used to get the ASCII code of each character. The `isupper` method is used to check if a character is upper-case.