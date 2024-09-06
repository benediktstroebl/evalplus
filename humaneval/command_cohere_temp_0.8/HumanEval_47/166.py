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
        # If the list has an odd number of elements, return the average of the middle element and the following element
        return (l[middle] + l[middle + 1]) / 2
```