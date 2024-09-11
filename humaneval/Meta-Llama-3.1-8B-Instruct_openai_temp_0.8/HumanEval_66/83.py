```python
def digitSum(s):
    """Returns the sum of ASCII codes of upper case characters in a string"""
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # => 0
print(digitSum("abAB"))  # => 131
print(digitSum("abcCd"))  # => 67
print(digitSum("helloE"))  # => 69
print(digitSum("woArBld"))  # => 131
print(digitSum("aAaaaXa"))  # => 153
```
This script defines a function `digitSum(s)` that calculates the sum of ASCII codes of upper case characters in the string `s`. The `ord()` function is used to get the ASCII code of each character, and a generator expression is used to iterate over the characters in the string and include only the ones that are upper case (checked using `isupper()`). The `sum()` function is then used to calculate the total sum. The test cases demonstrate the correct behavior of the function.