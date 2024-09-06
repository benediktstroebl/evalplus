```python
def sort_third(l):
    return l[:] * (len(l) // 3) + sorted(l)[len(l) // 3:][:len(l) // 3]
```

This solution uses some Python magic to keep the solution within a single line. The return statement uses slicing and concatenation to sort the values at indices divisible by three, while keeping the other values unchanged.