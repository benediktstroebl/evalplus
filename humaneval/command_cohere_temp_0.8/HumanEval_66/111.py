```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```
This function uses the sum function's capability to iterate over a string and calculate the sum of the upper ASCII characters it contains. The if statement filters out lowercase letters, ensuring the sum includes only digits. The resulting value is returned by the function.