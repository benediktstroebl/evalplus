```python
def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Check if the list has only one element
    if len(l) == 1:
        return l[0]
    # Sort the list
    sorted_l = sorted(l)
    # Find the middle element
    mid_index = len(sorted_l) // 2
    middle = sorted_l[mid_index]
    # Check if the number of elements is even
    if len(l) % 2 == 0:
        return middle
    # If the number of elements is odd, return the middle element
    return sorted_l[((len(sorted_l) + 1) // 2) - 1]
```