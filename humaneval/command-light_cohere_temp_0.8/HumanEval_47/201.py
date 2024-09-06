```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) < 3:
        return float('inf')  # return infinity since list is too small
    middle = len(l) // 2
    left = l[:middle]
    right = l[middle:]
    return (left[len(left)//2] + right[len(right)//2]) / 2
```