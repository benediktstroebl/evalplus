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
    
    # Find the middle index
    middle_idx = len(sorted_l) // 2

    if len(sorted_l) % 2 == 0:
        # If the list has an even number of elements, return the average of the two middle elements
        median = (sorted_l[middle_idx - 1] + sorted_l[middle_idx]) / 2
    else:
        # Otherwise, return the middle element
        median = sorted_l[middle_idx]
    
    return median
```

This function handles cases of empty lists, single-element lists, and even/odd-sized lists. It sorts the list first before determining the middle element or average of the middle elements. This ensures a consistent and expected behavior for various input lists.