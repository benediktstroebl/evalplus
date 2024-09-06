```python
def median(l):
    """Return median of elements in the list l"""
    if len(l) < 3:
        return float('inf') # return NaN for lists with fewer than 3 elements
    middle = l[len(l)//2]
    left = l[len(l)//2 - 1]
    right = l[len(l)//2]
    return (middle + left + right) / 3.0
```