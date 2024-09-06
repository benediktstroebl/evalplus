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

    # Find the median
    length = len(sorted_list)
    middle_index = length // 2

    if length % 2 == 0:
        # For an even number of elements, take the average of the two middle elements
        median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else:
        # For an odd number of elements, take the middle element
        median = sorted_list[middle_index]

    return median
```

This function handles cases of empty lists, single-element lists, and odd or even-length lists. It employs Python's built-in `sorted()` function to sort the list and then determines the median based on whether the list has an odd or even number of elements.