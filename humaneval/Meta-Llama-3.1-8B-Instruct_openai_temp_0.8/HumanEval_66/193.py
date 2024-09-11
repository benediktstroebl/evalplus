```python
def digitSum(s):
    """Returns the sum of the upper characters only ASCII codes in the input string."""
    return sum(ord(c) for c in s if c.isupper())

# Example use cases:
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
```

In this script:

- The function `digitSum(s)` takes a string `s` as input.
- It uses the `ord()` function to get the ASCII code of each character in the string.
- The `isupper()` method checks if a character is an uppercase letter.
- It uses a generator expression to filter the characters that are uppercase and sum their ASCII codes.
- The result is returned by the function.
- The example use cases demonstrate the function with different inputs and show the expected outputs.