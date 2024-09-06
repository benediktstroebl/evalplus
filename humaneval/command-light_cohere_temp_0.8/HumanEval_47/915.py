```python
def median(l: list):
    """Return median of elements in the list l.
    m = sorted(l)
    length = len(m)
    if length % 2 == 1:
        return (m[length // 2 - 1] + m[length // 2]) / 2
    else:
        return m[length // 2]
# Example usage
l = [-10, 4, 6, 1000, 10, 20]
print(median(l))  # Output: 15.0
```