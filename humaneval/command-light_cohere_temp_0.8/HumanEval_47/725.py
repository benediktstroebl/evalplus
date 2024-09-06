```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) < 1:
        return None  # No elements to calculate median for
    mid = len(l) // 2
    left_val = l[mid - 1]
    right_val = l[mid]
    return (left_val + right_val) / 2 if abs(left_val - right_val) <= 1 else None  # Another test to handle case where list is sorted
```