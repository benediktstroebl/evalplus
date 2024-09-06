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

    if len(sorted_l) % 2 == 0:
        # If the list has an even number of elements, return the average of the two middle elements
        median = (sorted_l[middle_index - 1] + sorted_l[middle_index]) / 2
    else:
        # Otherwise, return the middle element
        median = sorted_l[middle_index]
    
    return median
```

This function handles cases of empty lists, single-element lists, and odd or even-numbered lists, using efficient algorithms to sort and retrieve the middle element or middle two elements and returning the median.