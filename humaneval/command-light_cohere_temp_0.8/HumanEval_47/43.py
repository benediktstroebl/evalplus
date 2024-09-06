```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) > 1,
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

# Example usage:
result = median([-10, 4, 6, 1000, 10, 20])
assert result == 15.0
```