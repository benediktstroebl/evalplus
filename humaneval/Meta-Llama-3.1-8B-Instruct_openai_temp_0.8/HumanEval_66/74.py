```python
def digitSum(s):
    """Returns the sum of the ASCII codes of the upper case characters in a string."""
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

In this script, we define a function `digitSum` that uses a generator expression within the built-in `sum` function to calculate the sum of the ASCII codes of the upper case characters in the input string `s`. The `ord` function is used to get the ASCII code of each character, and the `isupper` method is used to check if a character is upper case. The test cases at the end demonstrate the function's behavior on various inputs.