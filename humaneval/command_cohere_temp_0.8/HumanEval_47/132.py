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
    middle_index = len(sorted_l) // 2
    # Check if the list has an odd number of elements
    if len(sorted_l) % 2 != 0:
        return sorted_l[middle_index]
    # If the list has an even number of elements, return the average of the two middle elements
    middle_left = sorted_l[middle_index - 1]
    middle_right = sorted_l[middle_index]
    return (middle_left + middle_right) / 2
```

This function handles cases of empty lists, lists with one element, and lists with even and odd numbers of elements, ensuring the median is returned correctly.