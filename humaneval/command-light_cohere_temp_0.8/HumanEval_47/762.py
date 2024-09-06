```python
def median(l):
    """Return median of elements in the list l"""
    if len(l) % 2 == 0:
        return (l[(len(l) / 2) - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

# Test suite
for i in range(0, 10):
    assert median([i, i+1]) == i + 1
```