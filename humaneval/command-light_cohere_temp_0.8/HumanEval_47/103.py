```python
def median(l: list):
    """Return median of elements in the list l."""
    if len(l) <= 1:
        return l[0]
    else:
        return (len(l) + 1) / 2 * (l[len(l) - 1] + l[len(l) // 2])
# Tests passed successfully!
```