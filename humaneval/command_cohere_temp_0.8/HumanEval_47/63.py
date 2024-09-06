```python
def median(l: list):
    """Return median of elements in the list l."""
    # Check if the list is empty
    if len(l) == 0:
        return None
    # Sort the list
    sorted_l = sorted(l)
    # Find the middle index
    middle_index = len(sorted_l) // 2
    if len(sorted_l) % 2 == 1:  # If odd number of elements
        return sorted_l[middle_index]
    else:  # If even number of elements
        middle_value1 = sorted_l[middle_index - 1]
        middle_value2 = sorted_l[middle_index]
        return (middle_value1 + middle_value2) / 2
```