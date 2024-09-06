```python
def median(l: list):
    """Return median of elements in the list l.
    assert(is):  # Test for empty list
    if len(l) == 0:
        return None  # Return None for empty list
    assert(all(type(x) == int for x in l)):  # Test for all elements in list l are integers
    mid = len(l) // 2
    left = [x for x in l if x < mid]
    right = [x for x in l if x >= mid]
    return (left + right) / 2 if len(l) % 2 != 0 else left[mid]
```