```python
def digitSum(string):
    return sum(ord(c) for c in string if c.isupper())
```