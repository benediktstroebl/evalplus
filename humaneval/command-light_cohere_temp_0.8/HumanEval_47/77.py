```python
def median(l: list):
    """Return median of elements in the list l.
    m = sorted(l)
    if len(m) % 2 == 1:
        return (m[(len(m) - 1) // 2])
    else:
        return (m[(len(m) - 1) // 2] + m[(len(m) - 1) // 2]) / 2.0
```
The function uses a sorting mechanism to identify the middle element(s) of a sorted list and calculates the median accordingly.