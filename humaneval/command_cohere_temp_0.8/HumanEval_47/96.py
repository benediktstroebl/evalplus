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

    # Finds the median
    mid_index = len(sorted_list) // 2
    if len(sorted_list) % 2 == 0:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    else:
        return sorted_list[mid_index]
```