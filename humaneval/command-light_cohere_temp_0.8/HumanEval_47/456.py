```python
def median(lst):
    n = len(lst) // 2 + 1
    if n == 1:
        return float('inf')
    return (lst[(n - 1) // 2] + lst[n // 2]) / 2
```