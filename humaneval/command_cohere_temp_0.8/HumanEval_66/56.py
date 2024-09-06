```python
def digitSum(s):
    return sum(ord(c) for c in s if c.isupper())
```

The function `digitSum` uses the `isupper` string method to selectively iterate over the upper-case characters present in the string `s`. For each character, it uses the `ord` function to get its ASCII code, then sums all these codes using the `sum` function.