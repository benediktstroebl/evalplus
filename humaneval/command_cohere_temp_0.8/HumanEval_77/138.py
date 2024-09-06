```python
def iscube(a):
    return a ** (1/3) == int(a ** (1/3))
```
This function simplifies the equation to a single cube root value, which is easier to test against integers.