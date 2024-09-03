```python
def digitSum(s):
    return sum(c for c in s if c.isupper())
return 0

# Tests
assertEqual(digitSum(""), 0)
assertEqual(digitSum("abAB"), 131)
assertEqual(digitSum("abcCd"), 67)
assertEqual(digitSum("helloE"), 69)
assertEqual(digitSum("woArBld"), 131)
assertEqual(digitSum("aAaaaXa"), 153)
```  This code defines a function **digitSum** that takes a string as input and returns the sum of the upper ASCII characters. It uses a testing methods to check its correctness against the provided examples.