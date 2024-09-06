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
    # Finds the index of the middle element
    middle_index = len(sorted_list) // 2
    # Check if the list has an odd number of elements, to return the middle element
    if len(sorted_list) % 2 != 0:
        return sorted_list[middle_index]
    # If the list has an even number of elements, return the average of the two middle elements
    mid_left = sorted_list[middle_index - 1]
    mid_right = sorted_list[middle_index]
    return (mid_left + mid_right) / 2
```

This function handles cases of empty lists and single-element lists, then employs Python's built-in sorting and indexing capabilities to find the middle element or elements for odd and even-length lists, respectively.

This solution assumes that the list elements are integers or floats — if the list contains other types of elements, the function may raise an error. Please adjust the function according to your list elements' data types if necessary.