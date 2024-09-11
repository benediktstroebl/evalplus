```python
def digitSum(s):
    """Returns the sum of ASCII codes of upper case characters in the input string."""
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # Expected output: 0
print(digitSum("abAB"))  # Expected output: 131
print(digitSum("abcCd"))  # Expected output: 67
print(digitSum("helloE"))  # Expected output: 69
print(digitSum("woArBld"))  # Expected output: 131
print(digitSum("aAaaaXa"))  # Expected output: 153
```

This script uses Python's built-in `ord` function to get the ASCII value of each character in the string, and the `isupper` method to check if the character is uppercase. The `sum` function is then used to calculate the sum of the ASCII codes of the upper case characters.