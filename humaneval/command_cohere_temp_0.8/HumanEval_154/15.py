```python
def cycpattern_check(a, b):
    a = a + a
    b = b + b
    return b in a
```

The function `cycpattern_check` takes two strings `a` and `b` as input and checks if the second word or any of its rotations are substring in the first word. The rotation trick helps us to solve this problem efficiently.