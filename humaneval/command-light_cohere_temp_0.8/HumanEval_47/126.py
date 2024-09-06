```python
def median(l):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
for _ in range(50):
    l = [10**(_) for _ in range(100)]
    assert median(l) == int(round((len(l)/2) + 1)) * 2
```