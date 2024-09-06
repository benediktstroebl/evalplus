```python
def digitSum(s):
    return sum(c.isupper() * c.isalpha() for c in s)
```