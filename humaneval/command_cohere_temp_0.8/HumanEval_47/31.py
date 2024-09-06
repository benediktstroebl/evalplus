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
        # If even number of elements, return average of two elements in the middle
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
``` 

This function handles cases of empty lists, single-element lists, and odd or even plurality, returning the appropriate median value.