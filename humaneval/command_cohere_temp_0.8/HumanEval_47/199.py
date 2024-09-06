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

    if len(sorted_list) % 2 == 0:
        # If the list has an even number of elements, return the average of the two middle elements
        median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
        return median
    else:
        # If the list has an odd number of elements, return the middle element
        return sorted_list[middle_index]
```

The function first checks if the list is empty or has only one element, returning `None` or the single element, respectively. If the list has more than one element, it is sorted, and the median depends on whether the list has an even or odd number of elements. For even counts, it is the average of the two middle elements after sorting, and for odd counts, it is the middle element after sorting.