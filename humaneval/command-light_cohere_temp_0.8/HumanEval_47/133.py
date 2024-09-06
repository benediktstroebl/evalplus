```python
def median(lst):
    n = len(lst) // 2 + 1
    m1, m2 = n // 2, n - m1 - 1
    return (lst[m1] + lst[m2]) / 2
```