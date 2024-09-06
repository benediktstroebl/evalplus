```python
def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Sort the list
    l.sort()
    # Find the middle element
    middle = len(l) // 2
    if len(l) % 2 == 0:
        return l[middle]
    else:
        return (l[middle - 1] + l[middle]) / 2
```