```python
def digitSum(string):
    return sum(ord(char) for char in string if char.isupper())
```