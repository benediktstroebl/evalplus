```python
def median(l):
    """Return median of elements in the list l."""
    return (len(l) + 1) / 2 * (sum(l[:len(l) // 2)] + sum(l[len(l) // 2:]))

# Test suite
for i in range(0, 10):
    assert median([i, i+1]) == i+1

for i in range(1, 10):
    assert median([-10, i, 6, 1000, 10, 20]) == i+1
```