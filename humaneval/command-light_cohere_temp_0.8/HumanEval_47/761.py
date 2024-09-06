```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list must be at least length.")
    if len(lst) == 1:
        return lst[0]
    m = len(lst) // 2 + 1
    mid1 = lst[m - 1]
    mid2 = lst[m]
    return (mid1 + mid2) / 2
```