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
    sorted_list = sorted(l)
    # Find the middle index
    middle_index = len(sorted_list) // 2
    # Check if the list has an odd number of elements
    if len(sorted_list) % 2 != 0:
        return sorted_list[middle_index]
    # If the list has an even number of elements, return the average of the two middle elements
    mid_left = sorted_list[middle_index - 1]
    mid_right = sorted_list[middle_index]
    return (mid_left + mid_right) / 2
```

This function handles cases of empty lists, single-element lists, and odd and even-numbered lists. It sorts the list first before determining the median, which is more efficient than averaging elements without sorting them when the list is even.