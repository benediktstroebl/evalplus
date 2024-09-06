```python
def median(l: list):
    n = len(l)
    m = n // 2
    if n % 2 == 1:
        return (l[m] + l[m - 1]) / 2
    else:
        return l[m]
```