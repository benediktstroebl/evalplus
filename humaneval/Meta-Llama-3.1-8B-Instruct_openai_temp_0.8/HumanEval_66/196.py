```python
def digitSum(s):
    """Returns the sum of the upper characters only' ASCII codes"""
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

- The `ord` function returns the ASCII code of a character.
- The `isupper` function returns `True` if a character is uppercase and `False` otherwise.
- We use a generator expression to iterate over the characters in the input string and only sum the ASCII codes of the uppercase characters.
- The `sum` function adds up the ASCII codes.