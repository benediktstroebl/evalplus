```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[0]) / 2
    else:
        return (lst[(n - 1) // 2] + lst[(n - 2) // 2]) / 2
```