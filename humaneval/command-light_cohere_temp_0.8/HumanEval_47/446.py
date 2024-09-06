```python
def median(l):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]
# Test the function
for i in range(0, 10):
    x = median([-10, i, 6, 1000, 10, 20])
    assert x == 15.0, "Error in median function."
```