```python
def digitSum(s):
    """Returns the sum of ASCII codes of upper characters in a string."""
    return sum(ord(char) for char in s if char.isupper())

# Test cases
print(digitSum("")) 
print(digitSum("abAB")) 
print(digitSum("abcCd")) 
print(digitSum("helloE")) 
print(digitSum("woArBld")) 
print(digitSum("aAaaaXa"))
```

In this script, we define a function `digitSum` that takes a string `s` as input. It uses a generator expression to iterate over each character in `s`, checks if the character is an upper case letter using `isupper()`, and if so, adds its ASCII code (`ord(char)`) to the sum. The result is returned by the function. We also include test cases to verify the function's correctness.