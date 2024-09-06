```python
def median(l: list):
    """Return median of elements in the list l.
    l = sorted(l)
    n = len(l)
    m = n // 2 + 1
    if n % 2 == 1:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]

# Test the median function
for i in range(0, 10):
    assert median([i, i+1]) == i+1
```