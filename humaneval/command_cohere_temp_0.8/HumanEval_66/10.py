```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```
This function uses the sum function's cumulative nature and the `isupper` string method to iterate through the string, determining the sum of uppercase ASCII characters. This allows the function to efficiently process the input string `s` and generate the desired result.

The task is to write a function that takes a string as input and returns the sum of the upper characters' ASCII codes. The code demonstrates how to solve this problem in Python using a self-contained function.