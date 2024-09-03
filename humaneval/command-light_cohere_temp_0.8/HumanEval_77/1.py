```python
def isCube(a):
    return (a != 0 and a * a * a > 1 and a * a * (a - 1) > 0) and a ** 3 == a ** 2
```