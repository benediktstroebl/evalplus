```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        raise ValueError("List is empty, cannot compute median")
    middle = len(l) >> 1
    if len(l) % 2 == 0:
        return (l[middle] + l[middle - 1]) / 2
    else:
        return l[middle]

# Test cases
median([3, 1, 2, 4, 5]) # 3
median([-10, 4, 6, 1000, 10, 20]) # 15
median([-5, -10, -15, -20, -25]) # Need implementation
```