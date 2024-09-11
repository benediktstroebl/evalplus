```python
def digitSum(s):
    """Returns the sum of the ASCII codes of upper case characters in the input string."""
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```
This script uses a generator expression to iterate over the characters in the input string `s`. For each character, it checks if it's an upper case character using the `isupper()` method. If it is, it calculates its ASCII code using the `ord()` function and adds it to the sum. The result is then returned by the function.