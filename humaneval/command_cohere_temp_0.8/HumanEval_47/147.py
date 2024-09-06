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

    # Finds the middle index
    middle_index = len(sorted_list) // 2

    if len(sorted_list) % 2 == 0:
        # If the list has an even number of elements, return the average of the two middle elements
        median = (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
        return median
    else:
        # If the list has an odd number of elements, return the middle element
        return sorted_list[middle_index]
``` 

This function handles cases of empty lists, lists with one element, and odd and even length lists. It sorts the list first before performing the median calculation for efficiency and consistency. Please note that this function assumes the list contains numeric values. For non-numeric values, a more complex logic may be required.