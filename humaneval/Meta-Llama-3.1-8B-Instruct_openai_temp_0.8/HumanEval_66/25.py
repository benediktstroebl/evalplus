```python
def digitSum(s):
    """Returns the sum of the ASCII codes of upper characters in the input string"""
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

This script uses a generator expression to iterate over the characters in the input string. The `ord` function returns the ASCII code of a character, and the `isupper` method checks if a character is uppercase. The `sum` function then adds up the ASCII codes of all uppercase characters.