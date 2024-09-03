```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing, False otherwise."""
    for i, x in enumerate(l):
        if x < l[i+1]:
            return False
    return True
```