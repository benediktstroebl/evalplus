```python
def digitSum(s):
    """Returns the sum of the ASCII codes of the upper characters only in the input string."""
    
    # Use a generator expression within the sum function to filter upper characters and sum their ASCII codes
    return sum(ord(c) for c in s if c.isupper())

# Test cases
print(digitSum(""))  # 0
print(digitSum("abAB"))  # 131
print(digitSum("abcCd"))  # 67
print(digitSum("helloE"))  # 69
print(digitSum("woArBld"))  # 131
print(digitSum("aAaaaXa"))  # 153
```

This script defines a function `digitSum` that takes a string `s` as input, filters out the upper characters using the `isupper` method, and returns the sum of their ASCII codes calculated using the `ord` function. The test cases demonstrate the function's correctness.