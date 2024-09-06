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
    num_elements = len(sorted_list)
    mid_index = num_elements // 2
    if num_elements % 2 == 1:
        # If odd number of elements, return the middle element
        return sorted_list[mid_index]
    else:
        # If even number of elements, return average of two middle elements
        middle1 = sorted_list[mid_index - 1]
        middle2 = sorted_list[mid_index]
        return (middle1 + middle2) / 2
```
The function first checks if the list is empty or has only one element, returning None or the single value, respectively. It then sorts the list and identifies the middle element(s), returning it (or them) as appropriate. This approach ensures a correct median value is always returned, handling both odd and even-numbered lists.